# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '1.2'

# Python Import:
import time
import sys

# Netmiko Import:
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import NetMikoTimeoutException
from netmiko.ssh_autodetect import SSHDetect
from netmiko import ConnectHandler
from paramiko import ssh_exception

# Logger import:
from messages.logger.logger import Logger

# Device model import:
from network.inventory.models.device_type import DeviceType
from network.inventory.models.device import Device

# Collect settings function import:
from system.settings.settings import collect_setting

# Logger class initiation:
logger = Logger('SSH Netconf connection')


# Main connection class:
class BaseConnection:
    """
    Basic connection class.
    
    Attributes:
    -----------------
    device_name:
        Xxx.
    device_hostname:
        Xxx.
    device_ssh_port:
        Xxx.
    device_https_port:
        Xxx.
    device_certificate:
        Xxx.
    device_username:
        Xxx.
    device_password:
        Xxx.
    device_type:
        Xxx.
    connection_status:
        Xxx.
    execution_time:
        Xxx.
    connection_timer:
        Xxx.
    supported_device:
        Xxx.
    repeat_connection:
        Xxx.
    repeat_connection_time:
        Xxx.
    """

    def __init__(self,
        device: Device,
        task_id: str = None,
        repeat_connection: int = 3,
        repeat_connection_time: int = 2,
    ) -> None:
        """
        Parameters:
        -----------------
        device: Device object
            Provided device object, to establish network connection.
        task_id: String
            Specifies the Celery task ID value, that will be added to logs messages.
        repeat_connection: Integer
            Specifies how many times the network connection will be retried.
        repeat_connection_time: Integer
            Determines how long the network connection will be attempted.
        """

        # Verify if the specified device variable is a valid Device object:
        if isinstance(device, Device):
            try:
                # Collect basic device data:
                self.device_certificate = device.certificate
                self.device_credential = device.credential
                self.device_https_port = device.https_port
                self.device_hostname = device.hostname
                self.device_ssh_port = device.ssh_port
                self.device_type = device.device_type
                self.device_token = device.token
                self.device_name = device.name
                self.device_object = device

                # Collect user data:
                if self.device_credential is None:
                    # Use default user data:
                    self.device_username = collect_setting('default_username', default='admin')
                    self.device_password = collect_setting('default_password', default='password')
                else: # Collect username and password from credential Model:
                    self.device_username = self.device_credential.username
                    self.device_password = self.device_credential.password

                # Device supported declaration:
                if self.device_type:
                    if self.device_type.name == 'Unsupported':
                        self.supported_device = False
                    else:
                        self.supported_device = True
                else:
                    self.supported_device = None

            except:
                raise TypeError('Provided device object is not compatible with connection class.')

        else:
            raise TypeError('The provided device variable must be a valid object of the Device class.')

        # Validate other provided data:
        self._validate_provided_data(task_id, repeat_connection, repeat_connection_time)

        # Connection declarations:
        self.connection_status = None
        self.connection = None
        # Connection timer declaration:
        self.connection_timer = None

    def __repr__(self) -> str:
        """ Connection class representation. """
        return f'<Class connection ({self.device_name}/{self.device_hostname})>'

    def __enter__(self) -> 'BaseConnection':
        """
        Use Connection class with python with command:

        with Connection(device) as connection:
            print(connection)

        Return:
        --------
            Connection class object.
        """
        
        try: # Try to start SSH connection:
            response = self.start_connection()
            if not response:
                raise
        except:
            if self.__exit__(*sys.exc_info()):
                pass
            else:
                raise
        else:
            # In case of success,
            # return Connection class object:
            return self

    def __exit__(self,
        exc_type,
        exc_value,
        exc_traceback,
    ):

        self.end_connection()

    def start_connection(self) -> 'BaseConnection':
        """
        Start a new SSH connection.

        Return:
        --------
            Connection class object.
        """

        # Check connection status:
        if not self.connection_status:
            
            # Check if device need autodetect device type:
            if self.supported_device is None:
                logger.info(f'Device type of the device: {self.device_name}, must be discovered.',
                    code_id='45366876978216757567883248573975',
                    execution=self.connection_timer,
                    object=self.device_object)
                # Update device type based on information collected via SSH protocol:
                update_device_type = self.update_device_type()
                # Connect to network device, if device type was collected:
                if update_device_type:
                    self._ssh_connect()
            else: # Connect to network device:
                self._ssh_connect()

            # Start connection timer if connected successfully established:
            if self.connection_status:
                # Start connection timer:
                self._start_connection_timer()
                # Return Connection class object:
                return self
            else: # Return False value:
                return False
        
        else: # Log that connection is already establish:
            logger.warning('Connection is already established.',
                code_id='20189872935982539885436854956290',
                execution=self.connection_timer,
                object=self.device_object)
            # Return Connection class object:
            return self
    
    def end_connection(self) -> None:
        """ 
        End current SSH connection.
        """

        # Check connection status:
        if self.connection_status:
            # Try to close SSH connection:
            try:
                self.connection.disconnect()
            except: # Log that connection is already ended:
                logger.warning('Connection is already ended.',
                    code_id='20189872935982539885436854956290',
                    execution=self.connection_timer,
                    object=self.device_object)
            else:
                # Log close of SSH connection:
                logger.info('SSH session ended.',
                    code_id='79237587073468678967477285487494',
                    execution=self.connection_timer,
                    object=self.device_object)
            finally:
                # End connection timer:
                self._end_connection_timer(logger)
        else: # Log that connection is already ended:
            logger.warning('Connection is already ended.',
                code_id='20189872935982539885436854956290',
                execution=self.connection_timer,
                object=self.device_object)

    def update_device_type(self) -> str:
        """
        Obtain network device type information using SSH protocol.
        And update Device type object.

        Return:
        --------
            Collected device type name.
        """

        # Log beginning of network device type checking process:
        logger.info(f'Started acquiring information about the type '\
            f'of device: {self.device_name}:{self.device_hostname}.',
            code_id='45987897427586734579937923758345',
            execution=self.connection_timer,
            object=self.device_object)

        # Connect to device to check device type, using SSH protocol:
        discovered_device_type_name = self._ssh_connect(autodetect=True)

        if discovered_device_type_name:

            try: # Collecting device type object:
                device_type_object = DeviceType.objects.get(netmiko_name=discovered_device_type_name) 
            except:
                # Log unsupported device type:
                logger.warning(f'Device type {discovered_device_type_name} '\
                    f'of device: {self.device_name}, is not supported.',
                    code_id='53984757569847568947569439023142',
                    execution=self.connection_timer,
                    object=self.device_object)
                # Change supported value to unsupported:
                self.supported_device = False
                try: # Try to collect unsupported device type:
                    device_type_object = DeviceType.objects.get(name='Unsupported')
                except:
                    logger.critical('Could not collect Unsupported device type.',
                        code_id='04930574037590847092843985739209',
                        execution=self.connection_timer,
                        object=self.device_object)
            else:
                # Log successful device type collection:
                logger.info(f'Device: {self.device_name}:{self.device_hostname} '\
                    f'is running {device_type_object.name} software.',
                    code_id='87394958738420432733295809238490',
                    execution=self.connection_timer,
                    object=self.device_object)
                # Change supported value to supported:
                self.supported_device = True
                # Change current device type to new one:
                self.device.device_type = device_type_object
                self.device_type = device_type_object

                try: # Try to update device type object:
                    self.device.save(update_fields=['device_type']) 
                except: # Return exception if there is a problem during
                    # the update of the device type object:
                    logger.critical(f'Exception occurs, durning device type update '\
                        f'process (device: {self.device_name}:{self.device_hostname}).',
                        code_id='45778589346798743750765946045895',
                        execution=self.connection_timer,
                        object=self.device_object)
                    # Return collected device type name:
                    return discovered_device_type_name
                else:
                    logger.info(f'Device type of device: {self.device_name}: '\
                        f'{self.device_hostname} has been updated.',
                        code_id='45827095295629370482756732094358',
                        execution=self.connection_timer,
                        object=self.device_object)

        else:

            # If connection attempt was unsuccessful, return False:
            return False

    def _validate_provided_data(self, task_id, repeat_connection, repeat_connection_time):
        """
        """

        # Verify if the specified taks_id variable is a string:
        if task_id is None or isinstance(task_id, str):
            # Celery task ID declaration:
            self.task_id = task_id
        else:
            raise TypeError('The provided task ID variable must be a string.')

        # Verify if the specified repeat connection variable is a integer:
        if repeat_connection is None or isinstance(repeat_connection, int):
            # Celery task ID declaration:
            self.repeat_connection = repeat_connection
        else:
            raise TypeError('The provided repeat connection variable must be a integer.')

        # Verify if the specified repeat connection time variable is a integer:
        if repeat_connection_time is None or isinstance(repeat_connection_time, int):
            # Celery task ID declaration:
            self.repeat_connection_time = repeat_connection_time
        else:
            raise TypeError('The provided repeat connection variable must be a integer.')

    def _start_execution_timer(self) -> float:
        """
        Start command execution time.

        Return:
        --------
            Method will return start time value.
        """

        # Start clock count:
        return time.perf_counter()

    def _end_execution_timer(self, start_time) -> float:
        """
        End command execution time counting.

        Return:
        --------
            Method will return execution end time value.
        """

        # Finish clock count & method execution time:
        finish_time = time.perf_counter()
        execution_time = round(finish_time - start_time, 5)

        # Return end execution time:
        return execution_time

    def _start_connection_timer(self) -> None:
        """
        Start connection time counting.
        """

        # Start clock count:
        self.connection_timer = time.perf_counter()

    def _end_connection_timer(self) -> float:
        """
        End connection time counting, and log result.

        Return:
        --------
            Method will return connection end time value.
        """

        # Check if connection timer is set up:
        if self.connection_timer:

            # Finish clock count & method execution time:
            finish_time = time.perf_counter()
            connection_timer = round(finish_time - self.connection_timer, 5)
            # Update global connection timer:
            self.connection_timer = connection_timer
            # Log time of SSH session:
            logger.info(f'SSH session was active for {self.connection_timer} seconds.',
                code_id='23345367424534254360995656646765',
                task_id=self.task_id,
                execution=self.connection_timer,
                object=self.device_object)
            # Reset connection timer:
            self.connection_timer = False

            # Return end connection time:
            return connection_timer

        else: # Raise error that connection timer is not set up:
            raise BrokenPipeError('The End connection timer method was '/
                'executed before the Start connection timer method or '/
                'after the connection timer value was reset.')

    def _sleep(self) -> None:
        """
        Sleep defined amount of time.
        """

        time.sleep(self.repeat_connection_time)

    def _ssh_connect(self, autodetect: bool = False) -> str:
        """ 
        Connect to device using SSH protocol.

        Parameters:
        -----------------
        commands: bool
            Detect device type.

        Return:
        --------
        The type of network device.
        """

        def log_connection_exception(connection_attempt, error):
            # Log error on last attempt:
            if connection_attempt == self.repeat_connection:
                # Log authentication exception:
                logger.error(f'Application was unable to establish SSH connection '\
                    f'to device: {self.device_name} (Last attempt). '\
                    f'Last error:\n{error}.',
                    code_id='93428735587384593649347783782395',
                    task_id=self.task_id,
                    execution=self.connection_timer,
                    object=self.device_object)
                # Change connection status to False.
                self.connection_status = False
                # Return False:
                return False
            else: # Log authentication exception:
                logger.error(f'Error occurred during SSH connection to device:'\
                    f' {self.device_name}:{self.device_hostname} '\
                    f'(Attempt: {connection_attempt}).\n{error}',
                    code_id='48753984592309457596283904835934',
                    task_id=self.task_id,
                    execution=self.connection_timer,
                    object=self.device_object)
                # Change connection status to False.
                self.connection_status = False

        # Check if device is supported before connection attempt:
        if self.supported_device is False:

            if not autodetect:
                logger.error(f'Device: {self.device_name}:{self.device_hostname}, is not supported.',
                    code_id='34893858374598734897479485769456',
                    task_id=self.task_id,
                    execution=self.connection_timer,
                    object=self.device_object)
            # Change connection status:
            self.connection_status = False

        elif self.supported_device or autodetect:

            # Performs a specified number of SSH connection attempts to network device.
            for connection_attempt in range(1, self.repeat_connection + 1):

                # Sleep before second and rest of conception attempts:
                if connection_attempt > 1:
                    self._sleep()

                # Log stat of a new SSH connection attempt:
                logger.info(f'SSH connection to device: {self.device_name}:{self.device_hostname}, '\
                    f'has been started (Attempt: {connection_attempt}).',
                    code_id='48734859373923718475395598735746',
                    task_id=self.task_id,
                    execution=self.connection_timer,
                    object=self.device_object)

                try: # Try connect to device, using SSH protocol:
                    # Check if the device type must be detected automatically:
                    if autodetect:
                        # Connect to device to check device type, using SSH protocol:
                        self.connection = SSHDetect(**{
                            'device_type': 'autodetect',
                            'host': self.device_hostname,
                            'port': self.device_ssh_port,
                            'username': self.device_username,
                            'password': self.device_password})
                    else:
                        # Connect to device, using SSH protocol:
                        self.connection = ConnectHandler(**{
                            'device_type': self.device_type.netmiko_name,
                            'host': self.device_hostname,
                            'port': self.device_ssh_port,
                            'username': self.device_username,
                            'password': self.device_password})

                # Handel SSH connection exceptions:
                except AuthenticationException as error:
                    # Log connection exception:
                    log_connection_exception(connection_attempt, error)
                except NetMikoTimeoutException as error:
                    # Log connection exception:
                    log_connection_exception(connection_attempt, error)
                except ssh_exception.SSHException as error:
                    # Log connection exception:
                    log_connection_exception(connection_attempt, error)
                except OSError as error:
                    # Log connection exception:
                    log_connection_exception(connection_attempt, error)
                except TypeError as error:
                    # Log connection exception:
                    log_connection_exception(connection_attempt, error)
                except ValueError as error:
                    # Log connection exception:
                    log_connection_exception(connection_attempt, error)

                else:
                    # Change connection status to True.
                    self.connection_status = True
                    # Log the start of a new connection:
                    logger.info(f'SSH connection to device: {self.device_name}:{self.device_hostname}, '\
                        f'has been established (Attempt: {connection_attempt}).',
                        code_id='48734859373923718475395598735746',
                        task_id=self.task_id,
                        execution=self.connection_timer,
                        object=self.device_object)
                    # if autodetect is True, collect device type name:
                    if autodetect:    
                        # Collect information about device type:
                        device_type = self.connection.autodetect()
                        self.connection_status = False
                        self.connection = False
                        return device_type
                    else: # Return connection:
                        return self.connection

            # Return connection status:
            return self.connection_status

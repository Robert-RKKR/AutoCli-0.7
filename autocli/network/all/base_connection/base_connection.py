# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '1.2'

# Python Import:
import time

# Logger import:
from messages.logger.logger import Logger

# Device model import:
from network.inventory.models.device import Device

# Collect settings function import:
from system.settings.settings import collect_setting

# Logger class initiation:
logger = Logger('SSH Netconf connection')


# Main connection class:
class Connection:
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
                self.device_https_port = device.https_port
                self.device_hostname = device.hostname
                self.device_ssh_port = device.ssh_port
                self.device_type = device.device_type
                self.device_token = device.token
                self.device_name = device.name
                self.device_object = device

                # Collect user data:
                if device.credential is None:
                    # Use default user data:
                    self.device_username = collect_setting('default_username', default='admin')
                    self.device_password = collect_setting('default_password', default='password')
                else: # Collect username and password from credential Model:
                    self.device_username = device.credential.username
                    self.device_password = device.credential.password

            except:
                raise TypeError('Provided device object is not compatible with connection class.')

        else:
            raise TypeError('The provided device variable must be a valid object of the Device class.')

        # Validate provided data:
        self._validate_provided_data(task_id, repeat_connection, repeat_connection_time)

        # Connection declarations:
        self.connection_status = None
        self.connection = None
        # Session timer declaration:
        self.connection_timer = None

        # Device supported declaration:
        if self.device_type:
            if self.device_type.name == 'Unsupported':
                self.supported_device = False
            else:
                self.supported_device = True
        else:
            self.supported_device = None

    def __repr__(self) -> str:
        """ Connection class representation. """
        return f'<Class connection ({self.device_name}/{self.device_hostname})>'

    def __enter__(self) -> 'Connection':
        """
        Use Connection class with python with command:

        with Connection(device) as connection:
            print(connection)

        """
        
        try: # Try to start SSH connection:
            self.start_connection()
        except:
            # In case of failure, return connection status:
            return self.connection_status
        else:
            # in case of success, return connection:
            return self.connection

    def __exit__(self,
        exc_type,
        exc_value,
        exc_traceback,
    ):

        self.close_connection()

    def start_connection(self):
        """
        Start a new SSH connection.
        """

        # Check if device need autodetect process:
        if self.supported_device is None:
            logger.info(f'Device type of device: {self.device_name}, must be discovered.',
                code_id='45366876978213248573975',
                execution=self.connection_timer,
                object=self.device_object,
            )
            # Update device type based on information collected via SSH protocol:
            self.update_device_type()
            # Connect to network device:
            self._ssh_connect()
        # Check connection status:
        elif not self.connection_status:
            self._ssh_connect()

        # Start connection timer if connected successfully:
        if self.connection_status:
            logger.info(
                f'SSH connection to device: {self.device_name}, has been established.',
                self.task_id, self.device_name)
            # Start session timer:
            self._start_connection_timer()
            return self
        else:
            return False
    
    def close_connection(self):
        """ 
        End current SSH connection.
        """

        # End connection timer:
        self._end_connection_timer()

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

    def _start_execution_timer(self):
        """
        Start command execution time.
        Method will return start time value.
        """

        # Start clock count:
        return time.perf_counter()

    def _end_execution_timer(self, start_time):
        """
        End command execution time counting.
        Method will return end time value.
        """

        # Finish clock count & method execution time:
        finish_time = time.perf_counter()
        execution_time = round(finish_time - start_time, 5)

        # Return end execution time:
        return execution_time

    def _start_connection_timer(self):
        """
        Start connection time counting.
        """

        # Start clock count:
        self.connection_timer = time.perf_counter()

    def _end_connection_timer(self):
        """
        End connection time counting, and log result.
        """

        # Finish clock count & method execution time:
        finish_time = time.perf_counter()
        self.connection_timer = round(finish_time - self.connection_timer, 5)

        # Log time of SSH session:
        logger.info(f'SSH session was active for {self.connection_timer} seconds.',
            code_id='233453674245342543646765',
            task_id=self.task_id,
            execution=self.connection_timer,
            object=self.device_object,
        )

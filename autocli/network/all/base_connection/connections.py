# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '1.1'

# Python import:
import concurrent.futures

# Connection class import:
from .connection import Connection

# Device model import:
from network.inventory.models.device import Device

# Settings import:
from system.settings.settings import collect_setting


# Connections class:
class Connections():
    """
    The class uses an SSH connection to connect to the
    multiple devices and perform available operations.
    
    Methods:
    -----------------
    start_connection:
        Start SSH connection with provided devices.
    end_connection:
        End current SSH connection.
    test_connection:
        Test connection to provided devices.
    update_device_type:
        Update provide devices type.
    send_enable:
        Send enabled command/s to provided devices,
        returns cli command/s output.
    send_enabled_dict:
        Send enabled command/s to provided devices,
        returns cli output and processed command/s data.
    send_config:
        Send configuration command/s to provided devices.
    execute_device_type_templates:
        Run all devices type template. available for provided
        devices. returns cli output and processed command/s data.
    send_config_dict:
        Not implemented yet.
    """

    def __init__(self,
        devices: list,
        task_id: str = None,
        repeat_connection: int = 2,
        repeat_connection_time: int = 2,
    ) -> None:
        """
        Parameters:
        -----------------
        device: List of device objects
            Provided list of device object, to establish network connection.
        task_id: String
            Specifies the Celery task ID value, that will be added to logs messages.
        repeat_connection: Integer
            Specifies how many times the network connection will be retried.
        repeat_connection_time: Integer
            Determines how long the network connection will be attempted.
        """

        # Main device data dictionary declaration:
        self.devices_data = {}
        
        # Validation some of provided data:
        self._validate_provided_data(task_id, repeat_connection, repeat_connection_time)

        # Validate provided devices list:
        for device in devices:
            # Verify if the provided device variable is a valid Device object:
            if isinstance(device, Device):
                # Create Connection class object:
                connection = Connection(device, self.task_id,
                    repeat_connection, repeat_connection_time)
                # Device data dictionary:
                device_data = {
                    'device_object': device,
                    'connection': connection}
                # Add device data to devices data dict:
                self.devices_data[device.name] = device_data
            else:
                raise TypeError('One of provided devices object is not '\
                    'compatible with connections class.')
        
    def __repr__(self) -> str:
        """
        Connections class representation.
        """
        return f'<Class connections ({self.devices_data})>'

    def __enter__(self) -> 'Connections':
        """
        Use Connection class with python with command:

        with Connection(device) as con:
            output = con.send_enable('show version')

        Return:
        --------
            Connection class object.
        """
        
        try: # Try to start SSH connection:
            self.start_connection()
        except:
            return False
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

    def start_connection(self) -> 'Connections':

        def start_connection_threadpoolexecutor(device_name):
            # Collect connection class object:
            connection = self.devices_data[device_name]['connection']
            # Start connection:
            connection.start_connection()

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=collect_setting('max_workers', default=10)) as executor:
            # Run connection execution function in Thread Pools with provided devices:
            executor.map(start_connection_threadpoolexecutor, self.devices_data)

    def end_connection(self) -> None:

        def end_connection_execution(device_name):
            
            # Collect connection class object:
            connection = self.devices_data[device_name]['connection']
            # Start connection:
            connection.end_connection()

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=collect_setting('max_workers', default=10)) as executor:
            # Run connection execution function in Thread Pools with provided devices:
            executor.map(end_connection_execution, self.devices_data)

    def send_enable(self, commands: str or list) -> dict:
        """
        Retrieves a string or list containing network CLI command/s,
        and sends them to a network device using SSH protocol.
        ! Usable only with enable levels commend/s.
        
        Parameters:
        -----------------
        commands: String
            Provided device object, to establish a SSH connection.
        commands: List
            Provided device object, to establish a SSH connection.

        Return:
        --------
        Dictionary containing command/s output.
        """

        # Declare final data output:
        output_data = {}

        def send_enable_threadpoolexecutor(device_name):
            # Collect connection class object:
            connection = self.devices_data[device_name]['connection']
            # Run send_enabled method:
            output = connection.send_enable(commands)
            # Return output data:
            return {device_name: output}

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=collect_setting('max_workers', default=10)) as executor:
            # Run send_enabled method for all network devices and collect response:
            for result in executor.map(send_enable_threadpoolexecutor,
                self.devices_data):
                # Add output to final data output:
                output_data.update(result)

        # Return output data:
        return output_data

    def send_config(self, commands: str or list) -> dict:
        """
        Retrieves a string or list containing network CLI command/s,
        and sends them to a network device using SSH protocol.
        ! Usable only with configuration terminal levels commends.
        
        Parameters:
        -----------------
        commands: String
            Provided device object, to establish a SSH connection.
        commands: List
            Provided device object, to establish a SSH connection.

        Return:
        --------
        String containing command/s output.
        """

        # Declare final data output:
        output_data = {}

        def send_enable_threadpoolexecutor(device_name):
            # Collect connection class object:
            connection = self.devices_data[device_name]['connection']
            # Run send_enabled method:
            output = connection.send_config(commands)
            # Return output data:
            return {device_name: output}

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=collect_setting('max_workers', default=10)) as executor:
            # Run send_enabled method for all network devices and collect response:
            for result in executor.map(send_enable_threadpoolexecutor,
                self.devices_data):
                # Add output to final data output:
                output_data.update(result)

        # Return output data:
        return output_data

    def send_enabled_dict(self, commands: str or list) -> dict:
        """
        Retrieves a string or list containing network CLI command/s,
        and sends them to a network device using SSH protocol.
        Collected commands are process to receive dictionary output,
        based on Device type templates.
        ! Usable only with enable levels commend/s.
        
        Parameters:
        -----------------
        commands: String
            Provided device object, to establish a SSH connection.
        commands: List
            Provided device object, to establish a SSH connection.

        Return:
        --------
        Dictionary containing command/s output and process data.
        """

        # Declare final data output:
        output_data = {}

        def send_enable_threadpoolexecutor(device_name):
            # Collect connection class object:
            connection = self.devices_data[device_name]['connection']
            # Run send_enabled method:
            output = connection.send_enabled_dict(commands)
            # Return output data:
            return {device_name: output}

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=collect_setting('max_workers', default=10)) as executor:
            # Run send_enabled method for all network devices and collect response:
            for result in executor.map(send_enable_threadpoolexecutor,
                self.devices_data):
                # Add output to final data output:
                output_data.update(result)

        # Return output data:
        return output_data

    def execute_device_type_templates(self) -> dict:
        """
        Collects all device type templates commands,
        and sends them to a network device using SSH protocol.
        Collected commands are process to receive dictionary output,
        based on Device type templates.
        ! Usable only with enable levels commend/s.
        """

        # Declare final data output:
        output_data = {}

        def send_enable_threadpoolexecutor(device_name):
            # Collect connection class object:
            connection = self.devices_data[device_name]['connection']
            # Run send_enabled method:
            output = connection.execute_device_type_templates()
            # Return output data:
            return {device_name: output}

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=collect_setting('max_workers', default=10)) as executor:
            # Run send_enabled method for all network devices and collect response:
            for result in executor.map(send_enable_threadpoolexecutor,
                self.devices_data):
                # Add output to final data output:
                output_data.update(result)

        # Return output data:
        return output_data

    def _validate_provided_data(self, task_id, repeat_connection, repeat_connection_time):
        """
        Validate provided data.
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

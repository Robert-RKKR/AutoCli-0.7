# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '1.1'

# Connection class import:
from .connection import Connection

# Device model import:
from network.inventory.models.device import Device


# Connections class:
class Connections():
    """
    """

    def __init__(self,
        devices: list,
        task_id: str = None,
        repeat_connection: int = 3,
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

        # Validate provided devices list:
        for device in devices:
            # Verify if the provided device variable is a valid Device object:
            if isinstance(device, Device):
                # Device data dictionary:
                device_data = {
                    'device_object': device}
                # Add device data to devices data dict:
                self.devices_data[device.name] = device_data
            else:
                raise TypeError('One of provided devices object is not '\
                    'compatible with connections class.')

        # Validation of the other provided data:
        self._validate_provided_data(task_id, repeat_connection, repeat_connection_time)
        
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
            response = self.start_connection()
            if not response:
                return False
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

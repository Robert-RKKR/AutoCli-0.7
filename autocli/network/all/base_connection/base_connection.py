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
        repeat_connection_time: int = 2
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

    def _validate_provided_data(self, data, isclass, ifnot):
        """
        """

        if data is None or isinstance(data, isclass):
            return data
        else:
            message = f''
            raise TypeError(message)

# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '2.1'

# Python Import:
import threading

# Base task Import:
from network.all.base_task.base_task import BaseTask

# Connection class Import:
from network.all.base_connection.connection import Connection

# Device model import:
from network.inventory.models.device import Device

# Celery application Import:
from autocli.celery import app


# Test taks class:
class CheckDeviceStatus(BaseTask):
    """
    Check status of device/s, using SSH / HTTPS protocol.
    Usage: CheckDeviceStatus.delay(<pk value>)

    Parameters:
    -----------------
    pk: integer, string or list
        int = return one device data collection.
        list = return multiple devices data collection.
        str 'all' = return all active devices data collection.
    """

    name = 'Check device status'
    description = 'Check status of device/s, using SSH / HTTPS protocol.'
    logger_name = 'Check device status'
    queue = 'status_check'

    def _run(self, pk, *args, **kwargs):
        # Try to collect all device objects based on provided pk value:
        try:
            if isinstance(pk, int):
                collected_devices = Device.objects.filter(pk=pk)
            elif isinstance(pk, list):
                collected_devices = Device.objects.filter(pk__in=pk)
            elif pk == 'all':
                collected_devices = Device.objects.all()
            else:
                raise TypeError('Provided PK value is not a integer, list or "all" string.')
        except:
            # Send message to channel:
            self.notification.send('Error occurs during device status update process.',
                notification=self.queue)
            # Log status update: 
            self.logger.warning(f'Error occurs during device collection (PK/s = {pk}).',
                code_id='48753847937689738679838884734686')
        else:
            # Collect all operation timer:
            self._start_execution_timer()
            # Define threads list:
            threads = list()
            # Iterate thru all collected device objects:
            for collected_device in collected_devices:

                # Run thread:
                thread = threading.Thread(target=self._check_device_status,
                    args=(collected_device,))
                # Add current thread to threads list:
                threads.append(thread)
                # Start current thread:
                thread.start()
            
            # Wait to end of all threads execution:
            for index, thread in enumerate(threads):
                thread.join()
            # Summary of the operations execution:
            end_operation = self._end_execution_timer()
            # Send notification:
            self.notification.send(f'Operation execution take {end_operation} seconds.',
                notification=self.queue)
            # Log end of process:
            self.logger.info(f'Operation execution take {end_operation} seconds.',
                code_id='48753847937689738679838884754565')

    def _check_device_status(self, device):

        # Collect device data:
        device_name = device.name

        # Connect to device using SSH protocol:
        ssh_connection = Connection(device, self.task_id, 1).test_connection()
        if ssh_connection:
            device.ssh_status = True
            # Prepare message:
            message = f'Status of device {device_name} was checked, device is active.'
        else:
            device.ssh_status = False
            # Prepare message:
            message = f'Status of device {device_name} was checked, device is not active.'
        # Update device object:
        device.save(update_fields=['ssh_status'])
        # Send notification:
        self.notification.send(message, object=device, notification=self.queue)
        # Log status update: 
        self.logger.info(message,
            code_id='48753847937689738679838884753456', object=device)

# Task registration:
CheckDeviceStatus = app.register_task(CheckDeviceStatus())

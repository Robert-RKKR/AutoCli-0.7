# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '2.1'

# Python import:
import threading

# Base task import:
from network.all.base_task.base_task import BaseTask

# Connection class import:
from network.all.base_connection.connection import Connection

# Device model import:
from network.inventory.models.device import Device

# Celery application import:
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
    message_name = 'Check device status'
    queue = 'status_check'

    def _run(self, pk: int or str or list, *args, **kwargs) -> None:

        # Define status values:
        self.active_devices = 0

        # Collect device/s based on provided pk value/s:
        collected_devices = self._collect_device_objects(pk)
       
        if collected_devices:
            # Start execution timer:
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
            # Summary of the operations time execution:
            operation_time = self._end_execution_timer()
            # Log end of process:
            self.logger.info(f'Status verification process '\
                f'has been completed, {self.active_devices} device/s '\
                f'from {len(collected_devices)}, is active. '\
                f'Process take {operation_time} seconds.',
                code_id='48753847937689738679838884754565')

    def _collect_device_objects(self, pk) -> Device:
        """
        Collect device/s based on provided pk value/s.
        """

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
            # Log status update: 
            self.logger.warning(f'Error occurs during device collection (PK/s = {pk}).',
                code_id='48753847937689738679838884734686')
            # Return False:
            return False
        else:
            # Return collected device/s:
            return collected_devices

    def _check_device_status(self, device) -> None:
        """
        Check status of provided device (SSH).
        """

        # Declare change value:
        changed = False
        # Collect device data:
        device_name = device.name
        # Log the start of the device status check process: 
        self.logger.info('Device status checking process of '\
            f'device {device_name} has begun',
            code_id='48753847937689738679838884753456', object=device)
        # Connect to device using SSH protocol:
        ssh_connection = Connection(device, self.task_id, 1).test_connection()
        # Change SSH device status and prepare message:
        if ssh_connection:
            # Change SSh device status:
            if device.ssh_status is False:
                device.ssh_status = True
                changed = True
            # Change status values:
            self.active_devices += 1
            # Prepare message:
            message = f'SSH status of device {device_name} was checked, device is active.'
        else:
            # Change SSh device status:
            if device.ssh_status is True:
                device.ssh_status = False
                changed = True
            # Prepare message:
            message = f'SSH status of device {device_name} was checked, device is not active.'
        # Update device object:
        if changed:
            device.save(update_fields=['ssh_status'])
        # Send user notification:
        self.notification.send(message, object=device, notification=self.queue)
        # Log status update:
        self.logger.info(message,
            code_id='48753847937689738679838884753456', object=device)

# Task registration:
CheckDeviceStatus = app.register_task(CheckDeviceStatus())

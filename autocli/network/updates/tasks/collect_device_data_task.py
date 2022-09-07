# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '2.1'

# Base task import:
from network.all.base_task.base_task import BaseTask

# Update models import:
from network.updates.models.collected_data import CollectedData
from network.updates.models.update import Update

# Device model import:
from network.inventory.models.device import Device


# Django exception import:
from django.db import IntegrityError

# NetCon import:
from network.all.base_connection.connection import Connection

# Celery application import:
from autocli.celery import app


# Test taks class:
class CollectDeviceDataTask(BaseTask):
    """
    Collect data from specified device or devices, using SSH protocol.
    Usage: CollectDeviceDataTask.delay(<pk value>)

    Parameters:
    -----------------
    pk: integer, string or list
        int = collecting data from one specific device, into data collection model.
        list = collecting data from provided devices, into data collection model.
        str 'all' = collecting data from all devices, into data collection model.
    
    Steps to follow:
    1. Collect all device objects based on provided pk value.
    2. Collect data from devices using SSH protocol.
    3. Create a new Device update object.
    4. Save collected data, into device collected data object.
    celery -A autocli worker -Q collect_data -l INFO
    """

    name = 'Collect device data'
    description = 'Collect data from specified device or devices, using SSH protocol.'
    logger_name = 'Collect device data'
    queue = 'collect_data'
    
    def _run(self, pk: int or str or list, *args, **kwargs) -> None:
        
        # Success counter:
        successful = 0
        # (Step: 1) Collect device/s based on provided pk value/s:
        collected_devices = self._collect_device_objects(pk)
        # Verify that the object was collected correctly:
        if collected_devices:

            # Start execution timer:
            self._start_execution_timer()
            # Iterate thru all collected device objects:
            for collected_device in collected_devices:
                
                # Start single operation clock counter:
                self._start_execution_timer()
                # Collect device data:
                device_name = collected_device.name
                # (Step: 2) Collect data from devices using SSH protocol:
                collected_data = self._collect_data_from_device(collected_device)
                
                # Check if device data has been collected correctly:
                if collected_data:
                    # (Step: 3) Create a new Device update object:
                    update_object = self._create_update_object(collected_device)
                    # (Step: 4) Save collected data, into device collected dada object:!!!!!!!!!!
                    if update_object:
                        output = self._save_to_device_collected_data(collected_data, update_object)
                        # Check output status:
                        if output:
                            # Raise successes command counter:
                            successful += 1
                        # update device update model status:
                        update_object.status = 1
                        update_object.result_status = True
                        update_object.save(update_fields=['status', 'result_status'])
                    else:
                        # update device update model status:
                        update_object.status = 2
                        update_object.result_status = False
                        update_object.save(update_fields=['status', 'result_status'])
                else:
                    # Create message:
                    message = f'Data could not be collected from device',\
                        f' {device_name} (NR. 37286274758).'
                    # Log data collection error:
                    self.logger.warning(message, self.task_id, device_name, True)
                    # Send message to channel:
                    self.send_message(message, self.queue)

            # Summary of the operations time execution:
            operation_time = self._end_execution_timer()
            # Create summary message:
            if successful == 1:
                # Create summary data collection process message:
                message = f'Process of collecting information from all requested devices '\
                f'has been accomplish (Successfully collected data from {successful} '\
                f'device out of {len(collected_devices)} requested device, '\
                f'in {operation_time} seconds).'
            elif successful > 1:
                # Create summary data collection process message:
                message = f'Process of collecting information from all requested devices '\
                f'has been accomplish (Successfully collected data from {successful} '\
                f'devices out of {len(collected_devices)} requested devices, '\
                f'in {operation_time} seconds).'
            else:
                # Create fails of data collection process message:
                message = f'Process of collecting information from all requested devices fails.' 
            # Log end of process:
            self.logger.info(message, self.task_id, None, True)
            # Send message to channel:
            self.send_message(message, self.queue)

        else:
            # Log data collection error:
            self.logger.warning('An error occurred during attempt to collect provided device/s, based on PK.',
                self.task_id, device_name)
            # Log data collection user error:
            self.logger.warning('An error occurred during data collection (NR. 374527153764).',
                self.task_id, device_name, True)

        # Return successful variable:
        return successful

    def _collect_data_from_device(self):
        pass

    def _create_update_object(self):
        pass

    def _save_to_device_collected_data(self):
        pass

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
        
# Task registration:
CollectDeviceDataTask = app.register_task(CollectDeviceDataTask())

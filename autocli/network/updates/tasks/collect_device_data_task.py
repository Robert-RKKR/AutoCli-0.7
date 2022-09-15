# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '2.1'

# Python import:
import concurrent.futures

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

# Settings import:
from system.settings.settings import collect_setting

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
    message_name = 'CollectDeviceDataTask'
    queue = 'collect_data'
    
    def _run(self, pk: int or str or list, *args, **kwargs) -> None:
        
        # Success counter:
        self.successful = 0
        # (Step: 1) Collect device/s based on provided pk value/s:
        collected_devices = self._collect_devices(pk)
        # Verify that the object was collected correctly:
        if collected_devices:

            # Start execution timer:
            start_execution_time = self._start_timer()

            with concurrent.futures.ThreadPoolExecutor(
                max_workers=collect_setting('max_workers', default=10)) as executor:
                # Run function in Thread Pools with provided devices:
                executor.map(self._single_thread_task, collected_devices)

            # Summary of the operations time execution:
            end_execution_time = self._end_timer(start_execution_time)
            # Create summary message:
            if self.successful > 0:
                # Create summary data collection process message:
                message = f'Process of collecting information from all requested devices '\
                f'has been accomplish successfully (Data was collected from: {self.successful} '\
                f'device/s out of: {len(collected_devices)} device/s, '\
                f'in {end_execution_time} seconds).'
            else: # Create fails of data collection process message:
                message = f'Process of collecting information from all requested devices fails.'
            # Log end of collection process:
            self.logger.info(message, code_id='48937458976893789679358237597436',
                execution=end_execution_time)
            # Send user notification:
            self.notification.send(message,
                notification=self.queue)

        else:
            # Send user notification:
            self.notification.send('An error occurred during data collection.',
                notification=self.queue)

        # Return successful variable:
        return self.successful

    def _single_thread_task(self, device):
        # Start single operation clock counter:
        start_operation_time = self._start_timer()
        # Collect device data:
        device_name = device.name
        # (Step: 2) Collect data from devices using SSH protocol:
        collected_data = self._collect_data_from_device(device)
        
        # Check if device data has been collected correctly:
        if collected_data:
            # (Step: 3) Create a new Device update object:
            update_object = self._create_update_object(device)
            # (Step: 4) Save collected data, into device collected dada object:
            if update_object:
                output = self._save_data_to_device_collected_data(
                    collected_data, update_object, device,
                    start_operation_time)
                # Check output status:
                if output:
                    # Raise successes command counter:
                    self.successful += 1
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
            message = f'Data could not be collected from device {device_name}.'
            # Log end of process:
            self.logger.info(message, object=device,
                code_id='58769376897345897428975345436546')
            # Send user notification:
            self.notification.send(message, object=device,
                notification=self.queue)

    def _save_data_to_device_collected_data(self,
        collected_data,
        update_object,
        device,
        start_operation_time) -> bool:
        """
        Save collected data to collect device data object.
        """

        # Defiant counts values:
        commands_count = len(collected_data)
        successes_command = 0
        # Iterate thru all collected commands:
        for single_command_output in collected_data:
            # Collect command data:
            command_data = collected_data[single_command_output]
            # Collect command data:
            command_name = command_data['command_name']
            command_raw_data = command_data['command_output']
            command_processed_data = command_data['processed_data']
            # Collect collected data status:
            raw_data_status = self._check_output_status(command_raw_data)
            processed_data_status = self._check_output_status(command_processed_data)
            # Check collected data operation status:
            if processed_data_status and raw_data_status:
                result_status = True
                # Raise successes command counter:
                successes_command += 1
            else:
                result_status = False

            try: # Try to create single device collected data object:
                CollectedData.objects.create(
                    # Update corelation:
                    update=update_object,
                    # Collected command data:
                    command_name=command_name,
                    command_raw_data=command_raw_data,
                    command_processed_data=command_processed_data,
                    # Collected command data status:
                    result_status=result_status,
                    raw_data_status=raw_data_status,
                    processed_data_status=processed_data_status,
                )
            except IntegrityError as error:
                # Log fails of data collection process:
                self.logger.warning(f'Process of creating device collected data object fails,'\
                    f' on device {device.name}.\n{error}',
                    code_id='38537459873486754845960739345664',
                    object=device)
                # Return False value
                return False

        # End operation timer:
        end_operation_time = self._end_timer(start_operation_time)

        # Log end of collected data saving process:
        if successes_command > 0:
            self.logger.info(f'The process of collecting data from {device.name} '\
                f'has been accomplish (Data was collected from: {successes_command} '
                f'commands outputs out of: {commands_count} commands). '\
                f'Execution time take: {end_operation_time} seconds.',
                code_id='38537459873486754845960739456456',
                execution=end_operation_time,
                object=device)
            return True
        else:
            self.logger.warning(f'The process of collecting data from '
                f'\{device.name} has failed. '\
                f'Execution time take: {end_operation_time} seconds.',
                code_id='38537459873486754556465465464566',
                execution=end_operation_time,
                object=device)
            return False

    def _create_update_object(self, device) -> Update:
        """
        Create a new Device update object.
        """

        # Declare update object variable:
        new_update_object = None

        try: # Try to create new update object:
            new_update_object = Update.objects.create(
                device=device, status=0)
        except IntegrityError as error:
            self.logger.warning(f'Process of creating device update object fails,'\
                f' on device {device.name}.\n{error}',
                code_id='38537459873486754845960739846464',
                    object=device)
            # Change update object variable to False:
            new_update_object = False

        # Return new update object:
        return new_update_object

    def _collect_data_from_device(self, device) -> dict:
        """
        Collect data from device using SSH protocol (NetCon class).
        """

        # Declare collected data variable:
        collected_data = None

        # Confect to device using NetCon class:
        connection = Connection(device, self.task_id).start_connection()
        # Check if connection was establish:
        if connection:
            # Collect all data from device:
            collected_data = connection.execute_device_type_templates()
            # Close SSH connection with device:
            connection.end_connection()
        else:
            # Change collect data variable to False:
            collected_data = False

        # Return all collected data:
        return collected_data

    def _collect_devices(self, pk: int or str or list) -> Device:
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

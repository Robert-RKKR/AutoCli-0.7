# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '1.0'

# Python import:
import concurrent.futures

# Base task import:
from network.all.base_task.base_task import BaseTask

# Update models import:
from network.updates.models.collected_data import CollectedData
from network.updates.models.update import Update

# Inventory models import:
from network.inventory.models.device_type_template import DeviceTypeTemplate

# Device model import:
from network.datasets.models.access_list_data import AccessListData
from network.datasets.models.arp_table_data import ArpTableData
from network.datasets.models.device_data import DeviceData
from network.datasets.models.dmvpn_data import DmvpnData
from network.datasets.models.environment_data import EnvironmentData
from network.datasets.models.etherchannel_data import EtherchannelData
from network.datasets.models.interface_data import InterfaceData
from network.datasets.models.mac_table_data import MacTableData
from network.datasets.models.module_data import ModuleData
from network.datasets.models.neighbor_data import NeighborData
from network.datasets.models.nhrp_data import NhrpData
from network.datasets.models.router_data import RouterData

# Django exception import:
from django.db import IntegrityError

# NetCon import:
from network.all.base_connection.connection import Connection

# Settings import:
from system.settings.settings import collect_setting

# Celery application import:
from autocli.celery import app

# Template type to device models:
DEVICE_DATA_CORRELATE = {
    0: ('None', None),
    1: ('Access list data', AccessListData),
    2: ('ARP table data', ArpTableData),
    3: ('Device data', DeviceData),
    4: ('DMVPN data', DmvpnData),
    5: ('Environment data', EnvironmentData),
    6: ('Etherchannel data', EtherchannelData),
    7: ('Interface data', InterfaceData),
    8: ('MAC table data', MacTableData),
    9: ('Module data', ModuleData),
    10: ('Neighbor data', NeighborData),
    11: ('NHRP data', NhrpData),
    12: ('Router data', RouterData),
}


# Test taks class:
class CorrelateCollectedDataTask(BaseTask):
    """
    Steps to follow:
    1. Collect lasted updates for all available devices.
    2. Collect all collected data based on collected updates.
    3. Convert collected data into device models.
    celery -A autocli worker -Q collect_data -l INFO
    
    """

    name = 'Correlate collected data'
    description = 'Correlate data collected from device, into database.'
    message_name = 'CorrelateCollectedData'
    queue = 'collect_data'
    
    def _run(self, *args, **kwargs) -> None:
        
        # Collect all newest updates:
        updates = self._collect_updates()
        if updates:
            # Iterate thru all collected updates:
            for update in updates:
                # Collect all collected data:
                collected_dates = self._collect_collected_data(update)
                # Iterate thru all collected data:
                for collected_data in collected_dates:
                    print('(collected_data)========> ', collected_data)
                    try: # Collect template:
                        template = DeviceTypeTemplate.objects.get(
                            device_type=update.device.device_type,
                            command=collected_data.command_name)
                        print('(template)========> ', template)
                    except:
                        pass
                    # 
                    self._data_correlation(
                        collected_data.command_processed_data,
                        template.device_data_corelation,
                        update)
            # Change correlated value in update model:
            # update.correlated = True
            # update.save(update_fields=['correlated'])
    
    def _data_correlation(self, command_processed_data, device_data_corelation, update):
        """
        """
        # 
        if device_data_corelation is 3:
            self._3_device_data(command_processed_data, update)

    def _3_device_data(self, command_processed_data, update):
        """
        """
        def correlate():
            # Correlated data:
            correlated_data = {}
            # Iterate thru all collected data:
            for data in command_processed_data:
                # Collect all model fields:
                fields = DeviceData._meta.get_fields()
                # Iterate thru all collected model fields:
                for field in fields:
                    # Collect field name:
                    field_name = field.name
                    field_name_upper = field.name.upper()
                    # Compare collected data to field name:
                    if field_name_upper in data:
                        correlated_data[field_name] = data[field_name_upper]
            return correlated_data

        # Corelate data:
        correlated_data = correlate()
        print('(correlated_data)========> ', correlated_data)
        # 
        try:
            device_data = DeviceData.objects.get(update=update)
        except:
            # Add update model:
            correlated_data['update'] = update
            DeviceData.objects.create(
                **correlated_data)
        else:
            device_data = DeviceData.objects.filter(update=update)
            device_data.update(**correlated_data)

    def _collect_updates(self) -> Update:
        """
        Collect newest update per all available devices.
        """
        # Updates list:
        all_updates = []
        # Collect all unique devices representation:
        devices_representation = Update.objects.order_by().values('device').distinct()
        # Iterate thru all collected devices:
        for device_representation in devices_representation:
            # Collect lasted update for provided device:
            try:
                update = Update.objects.filter(
                    device=device_representation['device'],
                    correlated=False
                ).latest('created')
            except:
                pass
            else:
                all_updates.append(update)
        # Return all collected updates list:
        return all_updates

    def _collect_collected_data(self, update) -> CollectedData:
        """
        Collect all available collected data per provided update.
        """
        # All collected data:
        all_collected_data = CollectedData.objects.filter(
            update=update,
            result_status=True)
        # Return all collected data:
        return all_collected_data
        
# Task registration:
CorrelateCollectedDataTask = app.register_task(CorrelateCollectedDataTask())

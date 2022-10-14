# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '1.0'

# Python import:
import concurrent.futures

# Base task import:
from network.all.base_task.base_task import BaseTask

# Update models import:
from network.updates.models.update import Update

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
DEVICE_DATA_CORRELATE = (
    (0, 'None', None),
    (1, 'Access list data', AccessListData),
    (2, 'ARP table data', ArpTableData),
    (3, 'Device data', DeviceData),
    (4, 'DMVPN data', DmvpnData),
    (5, 'Environment data', EnvironmentData),
    (6, 'Etherchannel data', EtherchannelData),
    (7, 'Interface data', InterfaceData),
    (8, 'MAC table data', MacTableData),
    (9, 'Module data', ModuleData),
    (10, 'Neighbor data', NeighborData),
    (11, 'NHRP data', NhrpData),
    (12, 'Router data', RouterData),
)


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

        pass

    def _collect_updates(self) -> Update:
        """
        """

        # Collect lasted updates for all available devices:
        updates = Update.objects.filter(
            'https://stackoverflow.com/questions/2411559/how-do-i-query-sql-for-a-latest-record-date-for-each-user'
        )
        
# Task registration:
CorrelateCollectedDataTask = app.register_task(CorrelateCollectedDataTask())

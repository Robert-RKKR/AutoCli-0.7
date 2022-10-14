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

# Device model import:
from .access_list_data import AccessListData
from .arp_table_data import ArpTableData
from .device_data import DeviceData
from .dmvpn_data import DmvpnData
from .environment_data import EnvironmentData
from .etherchannel_data import EtherchannelData
from .interface_data import InterfaceData
from .mac_table_data import MacTableData
from .module_data import ModuleData
from .neighbor_data import NeighborData
from .nhrp_data import NhrpData
from .router_data import RouterData

# Django exception import:
from django.db import IntegrityError

# NetCon import:
from network.all.base_connection.connection import Connection

# Settings import:
from system.settings.settings import collect_setting

# Celery application import:
from autocli.celery import app

# Template type to device models:
DEVICE_DATA_COORRELATE = (
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
    
    """

    name = 'Correlate collected data'
    description = 'Correlate data collected from device, into database.'
    message_name = 'CorrelateCollectedData'
    queue = 'collect_data'
    
    def _run(self, *args, **kwargs) -> None:

        pass
        
# Task registration:
CorrelateCollectedDataTask = app.register_task(CorrelateCollectedDataTask())

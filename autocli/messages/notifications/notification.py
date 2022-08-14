# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '1.0'

# Channels import:
from channels.layers import get_channel_layer

# Async import:
from asgiref.sync import async_to_sync

# Content import:
from messages.content.collect import collect_content_from_name

class Notification:
    """
    Notification class.

    Methods:
    --------
    xxx:
        xxx
    """

    # Channels registration:
    channel_layer = get_channel_layer()

    def channel_notification(self, message: str, **kwargs):
        """
        Create a new channel only notification based on the following data:

        Parameters:
        -----------------
        message: string
            Notification message string value.
        kwargs: dictionary
            It takes the following values:
                -object_id: xxx.
                -type: xxx.
        """

        async_to_sync(self.channel_layer.group_send)('notifications', {
            'type': 'send_collect',
            'message': message,
        })

    def send(self, message: str, **kwargs):
        """
        Create a new channel only notification based on the following data:

        Parameters:
        -----------------
        message: string
            Notification message string value.
        kwargs: dictionary
            It takes the following values:
                -app_name: xxx.
                -model_name: xxx.
                -object_id: xxx.
                -type: xxx.
        """

        pass

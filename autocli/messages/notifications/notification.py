# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '1.0'

# Channels import:
from channels.layers import get_channel_layer

# Async import:
from asgiref.sync import async_to_sync

# Content import:
from messages.content.collect import collect_content_from_name

# Notification model import:
from messages.notifications.models.notification import Notification as NotificationModel

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
            'link': 'For Future Use',
        })

    def database_notification(self, message: str, **kwargs):
        """
        Create a new database only notification based on the following data:

        Parameters:
        -----------------
        message: string
            Notification message string value.
        kwargs: dictionary
            It takes the following values:
                -type: xxx.
            -Information about content:
                -option I:
                    -app_name: Model application name.
                    -model_name: Model name.
                    -object_id: ID of log related object.
                -Option II:
                    -object: correlated object.
        """

        # Collect content type object if app_name and model_name was provided:
        if kwargs.get('object', False):
            # Collect content type based on object information:
            content_type = collect_content_from_name(
                app_name=kwargs['object'].__class__._meta.app_label,
                model_name=kwargs['object'].__class__.__name__,
            )
            # Add collected content type to dictionary:
            if content_type:
                kwargs['content_type'] = content_type
            else:
                raise TypeError('The provided object variable must be django model object.')
            # Collect object ID:
            try:
                kwargs['object_id'] = kwargs['object'].pk
            except:
                raise TypeError('The provided object variable must be django model object.')
        elif kwargs.get('app_name', False) and kwargs.get('model_name', False):
            # Collect content type based on provided information:
            content_type = collect_content_from_name(
                app_name=kwargs['app_name'],
                model_name=kwargs['model_name'],
            )
            # Add collected content type to dictionary:
            if content_type:
                kwargs['content_type'] = content_type
            else:
                raise TypeError('The provided object variable must be django model object.')

        NotificationModel.objects.create(
            content_type=kwargs.get('content_type', None),
            object_id=kwargs.get('object_id', None),
            type=kwargs.get('type', None),
            message=kwargs.get('message', None),
        )

    def send(self, message: str, **kwargs):
        """
        Create a new channel and database notification based on the following data:

        Parameters:
        -----------------
        message: string
            Notification message string value.
        kwargs: dictionary
            It takes the following values:
                -type: xxx.
            -Information about content:
                -option I:
                    -app_name: Model application name.
                    -model_name: Model name.
                    -object_id: ID of log related object.
                -Option II:
                    -object: correlated object.
        """

        self.channel_notification(message, **kwargs)
        self.database_notification(message, **kwargs)

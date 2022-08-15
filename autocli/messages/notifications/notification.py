# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '1.0'

# Channels import:
from channels.layers import get_channel_layer

# Async import:
from asgiref.sync import async_to_sync

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

        # Verify provided data:
        self._verification(**kwargs)

        # Collect content type object if app_name and model_name was provided:
        if kwargs.get('object', False):
            # Collect app and model name based on object information:
            kwargs['app_name'] = kwargs['object'].__class__._meta.app_label
            kwargs['model_name'] = kwargs['object'].__class__.__name__
            # Collect object ID:
            kwargs['object_id'] = kwargs['object'].id

        # Try to create notification:
        try:
            notification = NotificationModel.objects.create(
                content_type=kwargs.get('content_type', None),
                object_id=kwargs.get('object_id', None),
                type=kwargs.get('type', None),
                message=kwargs.get('message', None),
            )
        except:
            return False
        else:
            return notification

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
        return self.database_notification(message, **kwargs)

    def _verification(self, **kwargs):
        """ Provided data verification. """

        # Verify if the task_id variable is a valid sting:
        if kwargs.get('message', False):        
            if isinstance(kwargs['message'], str):
                if len(kwargs['message']) > 64:
                    raise ValueError('The provided message variable is to long (Allowed max 64 signs).')
            else:
                raise TypeError('The provided message variable must be string.')

        # Verify if the type variable is a valid sting:
        if kwargs.get('type', False):        
            if not isinstance(kwargs['type'], int):
                raise TypeError('The provided type variable must be integer.')

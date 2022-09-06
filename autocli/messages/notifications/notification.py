# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '1.0'

# Django import:
from django.db.models import Model

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
    channel_notification:
        Send notifications only through the channel.
    database_notification:
        Save notifications to the database only.
    send:
        Send notifications through the channel and
        save them to database.
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
                -type (Int): Type of notification.
                -object (Device object): Correlated object.
                -notification (Str): Notification channel name.
        """

        # Verify provided data:
        self._verification(**kwargs)

        # Check if object was provided:
        if kwargs.get('object', False):
            # Check if provided object is valid:
            if isinstance(kwargs['object'], Model):
                correlated_object = kwargs['object']
                async_to_sync(self.channel_layer.group_send)(kwargs['notification'], {
                    'type': 'send_collect',
                    'message': message,
                    'app_name': correlated_object.__class__._meta.app_label,
                    'model_name': correlated_object.__class__.__name__,
                    'object_id': correlated_object.pk,
                    'link': 'None'})
            else:
                raise TypeError('Provided object id not a valid Django object.')
        else: # If object is not valid raise TypeError:
            async_to_sync(self.channel_layer.group_send)(kwargs['notification'], {
                'type': 'send_collect',
                'message': message,
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
                -type (Int): Type of notification.
                -object (Device object): Correlated object.
        """

        # Verify provided data:
        self._verification(**kwargs)

        # Check if object was provided:
        if kwargs.get('object', False):
            # Check if provided object is valid:
            if isinstance(kwargs['object'], Model):
                correlated_object = kwargs['object']
                # Collect app and model name based on object information:
                kwargs['app_name'] = correlated_object.__class__._meta.app_label
                kwargs['model_name'] = correlated_object.__class__.__name__
                # Collect object ID:
                kwargs['object_id'] = correlated_object.id
            else: # If object is not valid raise TypeError:
                raise TypeError('Provided object id not a valid Django object.')
        
        # Try to create notification:
        try:
            notification = NotificationModel.objects.create(
                app_name=kwargs.get('app_name', None),
                model_name=kwargs.get('model_name', None),
                object_id=kwargs.get('object_id', None),
                type=kwargs.get('type', 0),
                message=message)
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
                -type (Int): Type of notification.
                -object (Device object): Correlated object.
                -notification (Str): Notification channel name.
        """

        self.channel_notification(message, **kwargs)
        return self.database_notification(message, **kwargs)

    def _verification(self, **kwargs):
        """
        Provided data verification.
        """

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

        # Verify if the type variable is a valid sting:
        if kwargs.get('notification', False):        
            if not isinstance(kwargs['notification'], str):
                raise TypeError('The provided notification variable must be string.')
        else:
            kwargs['notification'] = 'notification'

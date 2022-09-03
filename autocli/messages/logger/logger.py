# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '2.0'

# Application model Import:
from messages.logger.models.log import Log


# Settings import:
from django.conf import settings

# Severity constants declaration:
DEBUG = 5
INFO = 4
WARNING = 3
ERROR = 2
CRITICAL = 1

# Main Logger class:
class Logger:
    """
    Logger class.
    
    Attributes:
    -----------------
    application: Str
        Name of the application which triggered the log.

    Methods:
    --------
    critical:
        Create critical severity log.
    error:
        Create error severity log.
    warning:
        Create warning severity log.
    info:
        Create info severity log.
    debug:
        Create debug severity log.
    """

    def __init__(self, application: str = '--NoName--') -> None:
        """ Log application activity. """

        # Verify if the application variable is a valid sting:
        if isinstance(application, str):
            if len(application) <= 64:
                self.application = application
            else:
                raise ValueError('The provided application variable is to long (Allowed max 64 signs).')
        else:
            raise TypeError('The provided application variable must be string.')

        # Log data:
        self.log_data = None

    def critical(self, message: str, **kwargs):
        """
        Create a new log based on the following data:

        Parameters:
        -----------------
        message: string
            Logging message string value.
        kwargs: dictionary
            It takes the following values:
                -code_id: ID indicating the location of the log call in the code.
                -task_id: ID of the task associated with the log.
                -execution: Log task completion time.
                -Information about content:
                    -option I:
                        -app_name: Model application name.
                        -model_name: Model name.
                        -object_id: ID of log related object.
                    -Option II:
                        -object: correlated object.
            All additional values will be used to create log extension objects.
        """

        # Add data to kwargs dictionary:
        kwargs['severity'] = CRITICAL
        kwargs['message'] = message

        # Run process of log and details log creation:
        if settings.LOGGER_DEBUG:
            return self._run(**kwargs)

    def error(self, message: str, **kwargs):
        """
        Create a new log based on the following data:

        Parameters:
        -----------------
        message: string
            Logging message string value.
        kwargs: dictionary
            It takes the following values:
                -code_id: ID indicating the location of the log call in the code.
                -task_id: ID of the task associated with the log.
                -execution: Log task completion time.
                -Information about content:
                    -option I:
                        -app_name: Model application name.
                        -model_name: Model name.
                        -object_id: ID of log related object.
                    -Option II:
                        -object: correlated object.
            All additional values will be used to create log extension objects.
        """

        # Add data to kwargs dictionary:
        kwargs['severity'] = ERROR
        kwargs['message'] = message

        # Run process of log and details log creation:
        if settings.LOGGER_DEBUG:
            return self._run(**kwargs)

    def warning(self, message: str, **kwargs):
        """
        Create a new log based on the following data:

        Parameters:
        -----------------
        message: string
            Logging message string value.
        kwargs: dictionary
            It takes the following values:
                -code_id: ID indicating the location of the log call in the code.
                -task_id: ID of the task associated with the log.
                -execution: Log task completion time.
                -Information about content:
                    -option I:
                        -app_name: Model application name.
                        -model_name: Model name.
                        -object_id: ID of log related object.
                    -Option II:
                        -object: correlated object.
            All additional values will be used to create log extension objects.
        """

        # Add data to kwargs dictionary:
        kwargs['severity'] = WARNING
        kwargs['message'] = message

        # Run process of log and details log creation:
        if settings.LOGGER_DEBUG:
            return self._run(**kwargs)

    def info(self, message: str, **kwargs):
        """
        Create a new log based on the following data:

        Parameters:
        -----------------
        message: string
            Logging message string value.
        kwargs: dictionary
            It takes the following values:
                -code_id: ID indicating the location of the log call in the code.
                -task_id: ID of the task associated with the log.
                -execution: Log task completion time.
                -Information about content:
                    -option I:
                        -app_name: Model application name.
                        -model_name: Model name.
                        -object_id: ID of log related object.
                    -Option II:
                        -object: correlated object.
            All additional values will be used to create log extension objects.
        """

        # Add data to kwargs dictionary:
        kwargs['severity'] = INFO
        kwargs['message'] = message

        # Run process of log and details log creation:
        if settings.LOGGER_DEBUG:
            return self._run(**kwargs)

    def _verification(self, **kwargs):
        """ Provided data verification. """

        # Verify if the code_id variable is a valid sting:
        if kwargs.get('code_id', False):        
            if isinstance(kwargs['code_id'], str):
                if len(kwargs['code_id']) > 32:
                    raise ValueError('The provided code ID variable is to long (Allowed max 64 signs).')
            else:
                raise TypeError('The provided code ID variable must be string.')

        # Verify if the task_id variable is a valid sting:
        if kwargs.get('task_id', False):        
            if isinstance(kwargs['task_id'], str):
                if len(kwargs['task_id']) > 64:
                    raise ValueError('The provided task ID variable is to long (Allowed max 64 signs).')
            else:
                raise TypeError('The provided task ID variable must be string.')

        # Verify if the task_id variable is a valid sting:
        if kwargs.get('message', False):        
            if isinstance(kwargs['message'], str):
                if len(kwargs['message']) > 512:
                    raise ValueError('The provided message variable is to long (Allowed max 64 signs).')
            else:
                raise TypeError('The provided message variable must be string.')

        # Verify if the task_id variable is a valid sting:
        if kwargs.get('execution', False):        
            if not isinstance(kwargs['execution'], float):
                raise TypeError('The provided message variable must be float.')
    
    def _run(self, **kwargs):
        """ Run process of log and details log creation. """

        # Verify provided data:
        self._verification(**kwargs)

        # Collect content type object if app_name and model_name was provided:
        if kwargs.get('object', False):
            # Collect app and model name based on object information:
            kwargs['app_name'] = kwargs['object'].__class__._meta.app_label
            kwargs['model_name'] = kwargs['object'].__class__.__name__
            # Collect object ID:
            kwargs['object_id'] = kwargs['object'].id

        # Create new log based on provided data:
        return self._create_log(**kwargs)

    def _create_log(self, **kwargs):
        """ Create new log in Database. """

        # Collect all log data:
        self.log_data = {
            'application': self.application,
            'app_name': kwargs.get('app_name', 'None'),
            'model_name': kwargs.get('model_name', 'None'),
            'object_id': kwargs.get('object_id', None),
            'code_id': kwargs.get('code_id', None),
            'task_id': kwargs.get('task_id', None),
            'severity': kwargs.get('severity', None),
            'message': kwargs.get('message', None),
            'execution': kwargs.get('execution', None),
        }

        try: # Tyr to create a new log:
            new_log = Log.objects.create(**self.log_data)
        except:
            # If there was a problem during log creation process, return False:
            return False
        else:
            # Return created log object:
            return new_log

# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '2.0'

# Application model Import:
from logger.models.extension import Extension
from logger.models.log import Log

# Application model Import:
from core.models.content_type import ContentType

# Main Logger class:
class LoggerBase:
    """
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

    def _run(self, **kwargs):
        """ Run process of log and details log creation. """

        object_id = kwargs.get('object_id', False)
        content_type = kwargs.get('content_type', False)
        code_id = kwargs.get('code_id', False)
        task_id = kwargs.get('task_id', False)
        execution = kwargs.get('execution', False)
        message = kwargs.get('message', False)

        # Verify if the code_id variable is a valid sting:
        if code_id:        
            if isinstance(code_id, str):
                if len(code_id) > 64:
                    raise ValueError('The provided code ID variable is to long (Allowed max 64 signs).')
            else:
                raise TypeError('The provided code ID variable must be string.')

        # Verify if the task_id variable is a valid sting:
        if task_id:        
            if isinstance(task_id, str):
                if len(task_id) > 64:
                    raise ValueError('The provided task ID variable is to long (Allowed max 64 signs).')
            else:
                raise TypeError('The provided task ID variable must be string.')

        # Verify if the task_id variable is a valid sting:
        if message:        
            if isinstance(message, str):
                if len(message) > 64:
                    raise ValueError('The provided message variable is to long (Allowed max 64 signs).')
            else:
                raise TypeError('The provided message variable must be string.')

        # Verify if the correlated variable is a valid sting:
        if object_id:        
            if not isinstance(object_id, int):
                raise TypeError('The provided object ID variable must be integer.')

        # Verify if the correlated variable is a valid sting:
        if content_type:        
            if not isinstance(content_type, ContentType):
                raise TypeError('The provided content type variable must be content type object.')

        # Verify if the task_id variable is a valid sting:
        if execution:        
            if not isinstance(execution, float):
                raise TypeError('The provided message variable must be float.')

        # Exclude dictionary:
        exclude = {
            'correlated',
            'code_id',
            'task_id',
            'execution',
            'message',
            'severity',
        }
        # Run exclude dictionary to exclude used data:
        after_exclude = {x: kwargs[x] for x in kwargs if x not in exclude}

        # Create new log based on provided data:
        log = self._create_log(**kwargs)

        # Create log extension if additional data was provided:
        if after_exclude:
            # Create new log extension/s based on provided data:
            all_extensions = self._create_log_extensions(log, **after_exclude)

        # return log:
        return log

    def _create_log_extensions(self, log, **kwargs):
        """ Create new log extension in Database. """

        # New log extensions status dictionary:
        all_extensions = {}

        # Loop thru all provided data:
        for extension in kwargs:
        
            try: # Tyr to create a new log:
                new_extension = Extension.objects.create(
                    log=log,
                    name=extension,
                    data=kwargs[extension],
                )
            except:
                # If there was a problem during log creation process, return False:
                all_extensions[extension] = False
            else:
                # Return created log object:
                all_extensions[extension] = new_extension

        # Return all created log extensions:
        return all_extensions

    def _create_log(self, **kwargs):
        """ Create new log in Database. """

        # Define new log:
        new_log = None

        # Collect all log data:
        self.log_data = {
            'application': self.application,
            'correlated': kwargs.get('correlated', None),
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

# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '2.0'

# Import base logger:
from .logger_base import LoggerBase

# Severity constants declaration:
DEBUG = 5
INFO = 4
WARNING = 3
ERROR = 2
CRITICAL = 1

# Main Logger class:
class Logger(LoggerBase):
    """
    Logger class.
    
    Attributes:
    -----------------
    application:
        Xxx.
    user_log:
        Xxx.

    Methods:
    --------
    critical:
        Xxx.
    error:
        Xxx.
    warning:
        Xxx.
    info:
        Xxx.
    debug:
        Xxx.
    """

    def debug(self, message: str, **kwargs):
        """
        Create a new log based on the following data:

        Parameters:
        -----------------
        message: string
            Logging message string value.
        kwargs: dictionary
            It takes the following values:
                -correlated: Name of log related object.
                -code_id: ID indicating the location of the log call in the code.
                -task_id: ID of the task associated with the log.
                -execution: Log task completion time.
            All additional values will be used to create log extension objects.
        """

        # Add data to kwargs dictionary:
        kwargs['severity'] = DEBUG
        kwargs['message'] = message

        # Run process of log and details log creation:
        return self._run(**kwargs)

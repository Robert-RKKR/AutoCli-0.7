# Document description:
__author__ = 'Robert Tadeusz Kucharski'
__version__ = '2.0'

# Celery Import:
from celery import Task

# Python Import:
import time

# Application Import:
from messages.notifications.notification import Notification
from messages.logger.logger import Logger


# Base task class
class BaseTask(Task):

    # Basic celery attributes:
    ignore_result = False
    validation_class = ''
    public = True
    task_id = 'None'

    # Task identity attributes:
    description = ''
    name = 'default'
    queue = 'rkkr'

    # Define logger / notification name:
    message_name = 'BaseTask'

    def run(self, *args, **kwargs) -> None:
        # Logger initialization:
        self.logger = Logger(self.message_name)
        # Notification initialization:
        self.notification = Notification(self.message_name)
        # Collect process ID:
        self.task_id = self.request.id
        # Run task in delay:
        self._run(*args, **kwargs)

    def _run(self, *args, **kwargs) -> bool:
        return True

    def _start_timer(self) -> float:
        """
        Start task execution time counting.
        """

        # Return execution timer value:
        return time.perf_counter()

    def _end_timer(self, start_time) -> float:
        """
        End task execution time counting.
        """

        # Finish clock count & method execution time:
        finish_time = time.perf_counter()
        # Return execution timer value:
        return round(finish_time - start_time, 5)

    def _check_output_status(self, output) -> bool:
        if output == {} or output == [] or output is None or output is False:
            return False
        else:
            return True

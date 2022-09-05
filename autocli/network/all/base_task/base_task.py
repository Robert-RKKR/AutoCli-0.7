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

    # Correlated object data:
    corelate_object = None
    corelate_object_name = None

    # Task identity attributes:
    description = ''
    name = 'default'
    queue = 'rkkr'

    # Define logger name:
    logger_name = 'BaseTask'

    # Timer:
    execution_timer = None

    def run(self, *args, **kwargs) -> None:
        # Logger initialization:
        self.logger = Logger(self.logger_name)
        # Notification initialization:
        self.notification = Notification()
        # Collect process ID:
        self.task_id = self.request.id
        # Run task in delay:
        self._run(*args, **kwargs)

    def _run(self, *args, **kwargs) -> bool:
        return True

    def _start_execution_timer(self) -> float:
        """
        Start task execution time counting.
        """

        # Start clock count:
        self.execution_timer = time.perf_counter()
        # Return execution timer value:
        return self.execution_timer

    def _end_execution_timer(self) -> float:
        """
        End task execution time counting.
        """

        # Finish clock count & method execution time:
        finish_time = time.perf_counter()
        self.execution_timer = round(finish_time - self.execution_timer, 5)

        # Log time of SSH session:
        self.logger.info(f'The {self.name} task took {self.execution_timer} '\
            'seconds to complete.',
            code_id='84759346593467895673945000757890',
            task_id=self.task_id,
            execution=self.execution_timer,
            object=self.corelate_object_name)
        # Return execution timer value:
        return self.execution_timer

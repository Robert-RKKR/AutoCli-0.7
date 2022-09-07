# Django Import:
from django.db import models

# Manager Import:
from messages.logger.managers.log import LogManager

# Base model import:
from messages.all.base_model.base_model import BaseModel

# Constants:
SEVERITY = (
    (1, 'CRITICAL'),
    (2, 'ERROR'),
    (3, 'WARNING'),
    (4, 'INFO'),
    (5, 'DEBUG'),
)


# Logger models:
class Log(BaseModel):

    class Meta:
        
        # Model name values:
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'

        # Default ordering:
        ordering = ['-pk']

    # Model objects manager:
    objects = LogManager()

    # Log main data:
    application = models.CharField(
        verbose_name='Application',
        help_text='Name of the application which triggered the log.',
        max_length=64,
    )
    code_id = models.CharField(
        verbose_name='Code ID',
        help_text='ID indicating the location of the log call in the code.',
        max_length=32,
        null=True,
        blank=True,
    )
    task_id = models.CharField(
        verbose_name='Task ID',
        help_text='ID of the task associated with the log.',
        max_length=64,
        null=True,
        blank=True,
    )

    # Log severity:
    severity = models.IntegerField(
        verbose_name='Severity',
        help_text='Log severity.',
        choices=SEVERITY,
    )

    # Log data:
    message = models.CharField(
        verbose_name='Message',
        help_text='Log message.',
        max_length=512,
    )
    execution = models.FloatField(
        verbose_name='Execution time',
        help_text='Log task completion time.',
        null=True,
        blank=True,
    )

    # Model representation:
    def __str__(self) -> str:
        return f'{self.pk} - {self.message}'

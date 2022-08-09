# Django Import:
from django.db import models

# Constants:
SEVERITY = (
    (1, 'CRITICAL'),
    (2, 'ERROR'),
    (3, 'WARNING'),
    (4, 'INFO'),
    (5, 'DEBUG'),
)

# Logger models:
class Log(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = 'Log'
        verbose_name_plural = 'Logs',

    # Log timestamp:
    timestamp = models.DateTimeField(
        verbose_name='Timestamp',
        help_text='Time of log occurrence.',
        auto_now_add=True,
    )

    # Log corelation:
    application = models.CharField(
        verbose_name='Application',
        help_text='Name of the application which triggered the log.',
        max_length=64,
    )
    correlated_object = models.CharField(
        verbose_name='Correlated object',
        help_text='Name of log related object.',
        max_length=64, null=True,
    )
    code_id = models.CharField(
        verbose_name='Code ID',
        help_text='ID indicating the location of the log call in the code.',
        max_length=64,
        null=True,
    )
    task_id = models.CharField(
        verbose_name='Task ID',
        help_text='ID of the task associated with the log.',
        max_length=64,
        null=True,
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
        max_length=128,
    )
    execution_time = models.FloatField(
        verbose_name='Execution time',
        help_text='Log task completion time.',
    )

    # Model representation:
    def __str__(self) -> str:
        return f'{self.pk} - {self.message}'

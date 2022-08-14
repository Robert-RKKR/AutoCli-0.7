# Django Import:
from django.db import models

# Application models Import:
from .log import Log


# Logger models:
class Extension(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = 'Extension'
        verbose_name_plural = 'Extensions'

        # Default permissions:
        permissions = [('full')]

        # Default ordering:
        ordering = ['-pk']

    # Log corelation:
    log = models.ForeignKey(
        Log,
        verbose_name='Log',
        help_text='Log corelate with log extension.',
        on_delete=models.CASCADE,
    )

    # Extension data:
    name = models.CharField(
        verbose_name='Name',
        help_text='Extension name.',
        max_length=32,
    )
    data = models.TextField(
        verbose_name='Data',
        help_text='Extension data.',
    )

    # Model representation:
    def __str__(self) -> str:
        return f'{self.pk} - {self.log}/{self.name}'

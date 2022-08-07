# Django Import:
from django.db import models


# Device model:
class ContentType(models.Model):
    """ Xxx. """

    class Meta:
        # Model name values:
        verbose_name = 'Content type'
        verbose_name_plural = 'Content types'

        # Unique values:
        unique_together = [['app_name', 'model_name']]

    # Model information:
    app_name = models.CharField(
        verbose_name='Name',
        help_text='Object name.',
        max_length=128,
    )
    model_name = models.CharField(
        verbose_name='Name',
        help_text='Object name.',
        max_length=128,
    )

    # Model representation:
    def __repr__(self) -> str:
        return f'{self.pk}: {self.app_name}/{self.model_name}'

    def __str__(self) -> str:
        return f'{self.pk}: {self.app_name}/{self.model_name}'

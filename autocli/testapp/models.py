from django.db import models

# Django Import:
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# Create your models here.
class TestModel(models.Model):

    class Meta:
        
        # Model name values:
        verbose_name = 'TestModel'
        verbose_name_plural = 'TestModels'

    # Model status values:
    name = models.CharField(
        verbose_name='Name',
        help_text='Your ame.',
        max_length=32,
        blank=False,
    )
    test_value = models.BooleanField(
        verbose_name='Test value',
        help_text='Test model with root option cannot be deleted.',
        default=False,
    )
    description = models.TextField(
        verbose_name='Description',
        help_text='Status of test model object.',
    )

    def __init__(self, *args, **kwargs):
        super(TestModel, self).__init__(*args, **kwargs)
        self.__original_description = self.description

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        print(args, kwargs)
        if self.description != self.__original_description:
            print('--------ONE-------- ', self.description)
        else:
            print('--------TWO-------- ', self.description)

        super(TestModel, self).save(force_insert, force_update, *args, **kwargs)
        self.__original_description = self.description

    # Model representation:
    def __repr__(self) -> str:
        return f'{self.name}'

    def __str__(self) -> str:
        return  f'{self.name}'

# Signals:
@receiver(pre_save, sender=TestModel)
def re_signal(sender, instance, **kwargs):
    # print(f'=============== RKKR message! - pre_save\n{sender, instance, kwargs}')
    print('=============== ', instance.description,
        f'\nsender = {sender}',
        f'\ninstance = {instance}',
        f'\nkwargs = {kwargs}',
    )

@receiver(post_save, sender=TestModel)
def post_signal(sender, instance, created, **kwargs):
    # print(f'=============== RKKR message! - post_save\n{sender, instance, created, kwargs}')
    print('=============== ', instance.description,
        f'\nsender = {sender}',
        f'\ninstance = {instance}',
        f'\ncreated = {created}',
        f'\nkwargs = {kwargs}',
    )

# Django Import:
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# Model Import:
from testapp.models import TestModel

# # Signals:
# @receiver(pre_save, sender=TestModel)
# def re_signal(sender, instance, created, **kwargs):
#     print(f'=============== RKKR message! - pre_save\n{instance}')

# @receiver(post_save, sender=TestModel)
# def post_signal(sender, instance, created, **kwargs):
#     print(f'=============== RKKR message! - post_save\n{kwargs}')

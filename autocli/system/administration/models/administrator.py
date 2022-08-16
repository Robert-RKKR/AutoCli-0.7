# Django Import:
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

# Validator import:
from system.administration.validators import UsernameValidator

# Manager import:
from system.administration.managers import AdministratorManager


# Administrator model:
class Administrator(AbstractBaseUser, PermissionsMixin):

    class Meta:
        
        # Model name values:
        verbose_name = 'Administrator'
        verbose_name_plural = 'Administrators'

        # Default ordering:
        ordering = ['name']

    # Required model information:
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']
    objects = AdministratorManager()

    # Deleted information:
    deleted = models.BooleanField(
        verbose_name='Deleted',
        help_text='Is object deleted.',
        default=False,
    )

    # Model data time information:
    created = models.DateTimeField(
        verbose_name='Created',
        help_text='Object create date.',
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        verbose_name='Updated',
        help_text='object last update date.',
        auto_now=True,
    )
    last_login = models.DateTimeField(
        verbose_name='Last login',
        help_text='Administrator last login date.',
        blank=True,
        null=True
    )

    # Basic administrator fields:
    name = models.CharField(
        verbose_name='name',
        help_text='Administrator username.',
        max_length=32,
        unique=True,
        validators=[UsernameValidator],
        error_messages={
            'null': 'Name field is mandatory.',
            'blank': 'Name field is mandatory.',
            'unique': 'Administrator with this name already exists.',
            'invalid': 'Enter the correct name value. It must contain 3 to 32 digits, letters or special characters -, _ or spaces.',
        },
    )
    email = models.EmailField(
        verbose_name='E-mail address',
        help_text='Administrator e-mail address.',
        blank=True
    )
    is_staff = models.BooleanField(
        verbose_name='Staff status',
        help_text='Designates whether the user can log into this admin site.',
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name='Active',
        help_text='Designates whether this user should be treated as active.',
        default=True,
    )

    # Model representation:
    def __str__(self) -> str:
        return f'{self.pk} - {self.name}'
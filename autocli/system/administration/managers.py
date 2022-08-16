# Django Import:
from django.contrib.auth.base_user import BaseUserManager
from django.apps import apps


# Administrator manager:
class AdministratorManager(BaseUserManager):
    """
    Custom administrator model manager.
    """

    def create_user(self, name, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        # Set defaults values:
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        # Check if name and e-mail was provided:
        if not name:
            raise ValueError('The administrator name must be set.')
        if not email:
            raise ValueError('The Email must be set')

        # Collect administrator name:
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        name = GlobalUserModel.normalize_username(name)

        # Create base administrator account:
        user = self.model(
            name=name,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        # Set defaults values:
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        #
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        # Create super administrator account:
        return self.create_user(name, email, password, **extra_fields)

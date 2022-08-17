# Django import:
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Administrator permissions abstract model:
class AdministratorPermissions(PermissionsMixin):

    class Meta:
        abstract = True

    is_superuser = models.BooleanField(
        verbose_name='Super administrator',
        help_text='Is super administrator.',
        default=False,
    )
    user_permissions = None

# Django import:
from django.utils.deconstruct import deconstructible
from django.core import validators


@deconstructible
class NameValidator(validators.RegexValidator):
    regex = r'^[0-9,A-Z,a-z,-_ ]{3,32}$'
    message = 'The object name must contain 3 to 32 digits, letters and special characters -, _ or spaces.'
    flags = 0

from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

   
def release_date_validator(value):
    today = timezone.now().date()

    if value > today:
        raise ValidationError('Relase date cannot greater than today')

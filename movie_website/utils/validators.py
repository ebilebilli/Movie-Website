from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

   
def release_date_validator(value):
    today = timezone.now().date()

    if value > today:
        raise ValidationError('Relase date cannot greater than today')


def validate_birthday(value):
    today = timezone.now().date()
    min_allowed_date = today - timedelta(days=365 * 200) 
    min_allowed_age = today - timedelta(days=365 * 13)
    
    if isinstance(value, str):
        try:
            value = datetime.strptime(value, '%d-%m-%Y').date()
        except ValueError:
            raise ValidationError('Invalid date format. Use DD-MM-YYYY.')
    
    if value > today:
        raise ValidationError('Birthday cannot be in the future')
    
    if value > min_allowed_age:
        raise ValidationError('User must be at least 13 years old')
    
    if value < min_allowed_date:
        raise ValidationError('Birthday cannot be more than 100 years ago')

from django.core.exceptions import ValidationError


def username_validator(value):
    if len(value) < 2:
        raise ValidationError('The username must be a minimum of 2 chars')


def age_validator(value):
    if value < 18:
        raise ValidationError('Age must be above 18!')


def year_validator(value):
    if not 1980 <= value <= 2049:
        raise ValidationError('Year must be between 1980 and 2049')


def price_validator(value):
    if value < 1:
        raise ValidationError('Price must be above 1!')

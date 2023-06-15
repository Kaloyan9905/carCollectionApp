from django.core.validators import MinLengthValidator
from django.db import models

from carCollectionApp.web.validators import username_validator, age_validator, year_validator, price_validator


class Profile(models.Model):
    MIN_LEN_USERNAME = 2
    MAX_LEN_USERNAME = 10
    MAX_LEN_PASSWORD = 30
    MAX_LEN_FIRST_NAME = 30
    MAX_LEN_LAST_NAME = 30

    username = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_USERNAME,
        validators=(
            username_validator,
        )
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            age_validator,
        ),
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_PASSWORD,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LEN_FIRST_NAME,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_LEN_LAST_NAME,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    MAX_LEN_TYPE = 10
    MAX_LEN_MODEL = 20
    MIN_LEN_MODEL = 2

    CARS = (
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other'),
    )

    type = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_TYPE,
        choices=CARS,
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_MODEL,
        validators=(
            MinLengthValidator(2),
        ),
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            year_validator,
        ),
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            price_validator,
        ),
    )

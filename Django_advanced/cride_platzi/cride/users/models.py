"""User model."""

#django
from django.db import models
from django.contrib.auth.models import AbstracUser

#utilities
from cride.utils.models import CRideModel

class User(CRideModel, AbstracUser):
    """User model. 

    extend from Django`s Abstract User, change the username field
    yto email and add some extra fields.
    """
    email = models.EmailField(
        'email address',
        unique=True,
        error_message=(
            'unique' : 'A user with that email already exists'
        )
    )

    phone_number = models.CharField(max_length=12, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'laste_name']

    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'Help easily distinguish users and perfom queries. '
            'clients are the main type os user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to True when the user have verified its email address'
    )
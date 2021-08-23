'''https://docs.djangoproject.com/en/3.2/topics/auth/customizing/
'''

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .managers import MyUserManager


class MyUser(AbstractBaseUser):
    '''Override AbstractBaseUser.
    '''
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(blank=True)
    mobile_number = models.CharField(max_length=10)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.email)

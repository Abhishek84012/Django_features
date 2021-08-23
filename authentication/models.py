'''https://docs.djangoproject.com/en/3.2/topics/auth/customizing/
'''

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .managers import MyUserManager


class UserType(models.Model):
    CUSTOMER = 1
    SELLER = 2
    TYPE_CHOICE = (
        (SELLER, "Seller"),
        (CUSTOMER, "Customer")
    )
    id = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICE, primary_key=True)


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

    '''Achive multiple use types.
    '''
    # is_customer = models.BooleanField(default=True)
    # is_seller = models.BooleanField(default=True)

    # type = (
    #     (1,'Seller'),
    #     (2,'Customer')
    # )
    # user_type = models.IntegerField(choices=type,default=1)

    userType = models.ManyToManyField(UserType)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.email)

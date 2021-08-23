'''https://docs.djangoproject.com/en/3.2/topics/auth/customizing/
https://www.youtube.com/watch?v=UNx2F77IWMo&list=PLLz6Bi1mIXhEXEnfAgUJXB0vLjHkyee6q&index=9
'''

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .managers import MyUserManager

'''Achieve multiple use types through below different three ways(if exists all same field).
'''
# class UserType(models.Model):
#     CUSTOMER = 1
#     SELLER = 2
#     TYPE_CHOICE = (
#         (SELLER, "Seller"),
#         (CUSTOMER, "Customer")
#     )
#     id = models.PositiveSmallIntegerField(
#         choices=TYPE_CHOICE, primary_key=True)

#     def __str__(self):
#         return self.get_id_display()

'''Achieve multiple use types through below different three ways(if exists different field).
'''

# class Customer(models.Model):
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     address = models.CharField(max_length=1000)


# class Seller(models.Model):
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     gst = models.CharField(max_length=100)
#     warehouse_location = models.CharField(max_length=1000)


class CustomerAdditional(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=1000)


class SellerAdditional(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gst = models.CharField(max_length=100)
    warehouse_location = models.CharField(max_length=1000)


class MyUser(AbstractBaseUser):
    '''Override AbstractBaseUser.
    '''
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    mobile_number = models.CharField(max_length=10, null=True, blank=True)

    '''Achieve multiple use types through below different three ways(if exists all same field).
    '''
    # is_customer = models.BooleanField(default=True)
    # is_seller = models.BooleanField(default=False)

    # type = (
    #     (1,'Seller'),
    #     (2,'Customer')
    # )
    # user_type = models.IntegerField(choices=type,default=1)

    # userType = models.ManyToManyField(UserType)

    '''Achieve multiple use types through below ways(Proxy Modal)(if exists all different field).
    '''
    class Types(models.TextChoices):
        SELLER = "seller", "SELLER"
        CUSTOMER = "customer", "CUSTOMER"

    default_type = Types.CUSTOMER
    type = models.CharField(
        max_length=255, choices=Types.choices, default=default_type)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.default_type
        return super().save(*args, **kwargs)


# Modal managers for proxy models.
class SellerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=MyUser.Types.SELLER)


class CustomerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=MyUser.Types.CUSTOMER)


class Seller(MyUser):
    default_type = MyUser.Types.SELLER
    objects = SellerManager()

    class Meta:
        proxy = True

    def sell(self):
        print("I can sell")

    @property
    def sell_additional(self):
        return self.SellerAdditional


class Customer(MyUser):
    default_type = MyUser.Types.CUSTOMER
    objects = CustomerManager()

    class Meta:
        proxy = True

    def buy(self):
        print("I Can Buy")

    @property
    def sell_additional(self):
        return self.SellerAdditional

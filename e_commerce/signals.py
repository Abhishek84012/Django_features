from django.core.signals import request_finished
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from e_commerce.models import Product


@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")


@receiver(pre_save, sender=Product)
def my_handler(sender, **kwargs):
    print("Pre save signal called...")


@receiver(post_save, sender=Product)
def my_handler(sender, **kwargs):
    print("Post save signal called...")

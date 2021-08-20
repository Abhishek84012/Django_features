from django.contrib import admin

from .models import Cart, Product, ProductInCart

admin.site.register(Product)
admin.site.register(ProductInCart)
admin.site.register(Cart)

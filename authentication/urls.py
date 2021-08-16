'''https://dev.to/yahaya_hk/password-reset-views-in-django-2gf2
'''
from django.urls import path

from . import views

urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name="sign-up"),

]

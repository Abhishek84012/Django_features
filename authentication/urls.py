from django.urls import path

from . import views

urlpatterns = [
    path('sign-up-customer/', views.CustomerSignUpView.as_view(),
         name="sign-up-customer"),
    path('sign-up-seller/', views.SellerSignUpView.as_view(), name="sign-up-seller"),

]

from django.urls import path

from . import views

urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name="sign-up"),
    path('sign-up-seller/', views.SignUpViewForSeller.as_view(), name="sign-up-seller"),

]

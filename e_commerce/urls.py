from django.urls import path

from e_commerce import views

urlpatterns = [
    path('index/', views.index.as_view(), name="index"),
]

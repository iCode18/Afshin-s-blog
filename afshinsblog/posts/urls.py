#use seprated url file to have clean and more mangable
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

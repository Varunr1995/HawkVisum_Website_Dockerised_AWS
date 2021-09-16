from django.urls import path
from . import views

urlpatterns = [path("", views.careerspage, name='careerspage')]

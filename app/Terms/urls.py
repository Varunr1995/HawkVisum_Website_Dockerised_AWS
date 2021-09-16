from django.urls import path
from . import views

urlpatterns = [path("", views.termspage, name='termspage')]

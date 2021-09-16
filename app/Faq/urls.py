from django.urls import path
from . import views

urlpatterns = [path("", views.faqpage, name='faqpage')]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.industriespage, name='industriespage'),
    path("education/", views.educationpage, name='educationpage'),
    path("automobile/", views.automobilepage, name='automobilepage'),
    path("health/", views.healthpage, name='healthpage'),
    path("construction/", views.constructionpage, name='constructionpage'),
    path("industrial/", views.industrialpage, name='industrialpage'),
    path("gaming/", views.gamingpage, name='gamingpage'),
    path("interiordesigning/", views.interiordesigningpage,
         name='interiordesigningpage')
    ]

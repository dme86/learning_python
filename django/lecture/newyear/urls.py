from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="index")         # single, empty route will load index function
]

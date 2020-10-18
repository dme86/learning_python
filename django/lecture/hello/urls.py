from django.urls import path
from . import views                             # import views(.py) from doc root

urlpatterns = [
        path("", views.index, name="index")     # empty url should show index from views, named as index
]

from django.urls import path
from . import views                             # import views(.py) from doc root

urlpatterns = [
        path("", views.index, name="index"),    # empty url(default route) should show index from views, named as index
        path("dan", views.dan, name="dan")      # load dan path for http://127.0.0.1:8000/hello/dan
]

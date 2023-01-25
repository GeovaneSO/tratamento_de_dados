from django.urls import path
from .views import upload, home

urlpatterns = [
    path("", home, name='home'),
    path("files/", upload, name='upload'),
]

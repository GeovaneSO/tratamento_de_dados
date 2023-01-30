from django.urls import path
from .views import upload, home, register, login
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", home, name="home"),
    path("files/", upload, name="upload"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
]

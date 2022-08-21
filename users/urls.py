from django.urls import path
from rest_framework.authtoken import views

from .views import UserLogout, UserRegister, LoginView

# users/
urlpatterns = [
    path("signup/", UserRegister.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", UserLogout.as_view()),
]
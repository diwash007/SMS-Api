from argparse import Namespace
from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('', views.StudentViewSet.as_view()),
]
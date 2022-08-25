from argparse import Namespace
from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('students/', views.StudentList.as_view()),
    path('students/<int:pk>/', views.StudentDetail.as_view()),
]
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

from .serializers import StudentSerializer
from .models import Student


class StudentList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


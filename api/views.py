from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import StudentSerializer
from .models import Student


class StudentViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        students = Student.objects.all()
        print(students)
        serializer = StudentSerializer(students)
        return Response(serializer.data)

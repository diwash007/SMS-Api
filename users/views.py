from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response

from django.forms import ValidationError
from django.contrib.auth import login, authenticate

from users.serializers import UserSerializer

from .models import User

# Create your views here.
class UserRegister(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        ser = UserSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)


class LoginView(APIView):
    def post(self, request, format=None):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserLogout(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Successfully logged out."})
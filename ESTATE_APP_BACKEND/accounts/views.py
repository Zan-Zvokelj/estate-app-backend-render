from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.authtoken.models import Token
# Create your views here.
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import UserRegistrationSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        print(f"User:{user}")
        print(f"Token:{token.key}")
        return Response({
            'token': token.key,
            'username': user.username,
            'user_id': user.pk,
            'email': user.email
        })


class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny] 

    def perform_create(self, serializer):
        password = make_password(serializer.validated_data['password']) 
        serializer.save(password=password)  
from django.shortcuts import render
from djoser.conf import User
from rest_framework import generics
# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated

from _auth.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer




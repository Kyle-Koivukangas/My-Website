# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .models import User
from .serializers import UserSerializer

# Lists all users or creates a new one
# uses DRF ListCreateAPIView base class for get and create functionality right out of the box
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# show info for just one user
# Uses DRF RetrieveUpdateDestroyAPIView base class for retrieve, update, and destroy functionality right out of the box
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


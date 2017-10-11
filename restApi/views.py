# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer


class UserList(APIView):

    def get(self, request):
        users = User.objects.all()
        #serialize/convert to JSON, can't send python objects in an HTTP response
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self):

        pass



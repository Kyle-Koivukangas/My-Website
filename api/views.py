from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from api.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    Projects API endpoint.
    """
    queryset = Group.objects.all()
    serializer_class = ProjectSerializer
    

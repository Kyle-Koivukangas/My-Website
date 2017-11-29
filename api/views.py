from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from api.serializers import UserSerializer, GroupSerializer, ProjectSerializer
from api.models import Project

@permission_classes((IsAdminUser, ))
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

@permission_classes((IsAdminUser, ))
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@permission_classes((IsAuthenticatedOrReadOnly, ))
class ProjectViewSet(viewsets.ModelViewSet):
    """
    Projects API endpoint.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

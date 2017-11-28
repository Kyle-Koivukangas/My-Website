from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api.models import Project

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('url', 'date', 'project_name', 'description', 'text', 'image')

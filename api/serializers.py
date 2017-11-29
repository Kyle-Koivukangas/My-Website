from django.contrib.auth.models import User, Group
from rest_framework import serializers
from datetime import datetime

from api.models import Project


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

# class ProjectSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'date', 'project_name', 'description', 'text', 'image')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('date', 'project_name', 'description', 'text', 'image')

    # date = serializers.DateTimeField(default=datetime.now())
    # project_name = serializers.CharField(max_length=50)
    # description = serializers.CharField(max_length=250)
    # text = serializers.CharField(max_length=1000)
    # image = serializers.ImageField()

    # def create(self, validated_data):
    #     return Project(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.date = validated_data.get('date', instance.date)
    #     instance.project_name = validated_data.get('project_name', instance.project_name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.text = validated_data.get('text', instance.text)
    #     instance.image = validated_data.get('image', instance.image)
    #     return instance
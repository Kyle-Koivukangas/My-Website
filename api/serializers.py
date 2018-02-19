from django.contrib.auth.models import User, Group
from rest_framework import serializers
from datetime import datetime
from mezzanine.blog.models import BlogPost

from api.models import Project


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('date', 'name', 'slug', 'description', 'text', 'image')

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'content', 'publish_date', 'expiry_date', 'status')


# class BlogPostSerializer(serializers.RelatedField):

#     def to_representation(self, value):
#         if isinstance(value, models.BlogPost):
#             serializer = BookmarkSerializer(value)
#         else:
#             raise Exception('Unexcepted type of tagged object')

#         return serializer.data
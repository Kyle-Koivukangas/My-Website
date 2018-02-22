from django.contrib.auth.models import User, Group
from rest_framework import serializers
from datetime import datetime
from mezzanine.blog.models import BlogPost
from mezzanine.generic.models import ThreadedComment
# from django_commments.models import Comment

from api.models import Project
# from api.views import ThreadedCommentViewSet


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
    # comments = ThreadedCommentSerializer(many=True, read_only=True)
    comments = serializers.SerializerMethodField()
    related_posts = serializers.StringRelatedField(many=True)
    keywords = serializers.StringRelatedField(many=True)

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'slug', 'content', 'publish_date',
                  'expiry_date', 'related_posts',
                  'featured_image', 'status', '_meta_title',
                  'description', 'keywords', 'comments',)

    def get_comments(self, obj):
        # result = str(obj.comments.all())
        result = []
        for comment in obj.comments.all():
            comment_data = {
                "id": comment.id,
                "user_name": comment.user_name,
                "comment": comment.comment,
                "replied_to": comment.replied_to.id if comment.replied_to is not None else 0,
                "replied_to_content": str(comment.replied_to),
                "submit_date": comment.submit_date,
                "by_blog_author": comment.by_author
            }
            
            if comment.is_public and not comment.is_removed:
                result.append(comment_data)
            else:
                comment_data = {}
                continue

        return result

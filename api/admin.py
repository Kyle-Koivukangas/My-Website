from django.contrib import admin
from mezzanine.blog.models import BlogPost

from api.models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['date', 'name', 'description', 'text', 'image']

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['categories', 'allow_comments', 'comments', 'rating', 'featured_image', 'related_posts', 'admin_thumb_field']

admin.site.register(Project, ProjectAdmin)

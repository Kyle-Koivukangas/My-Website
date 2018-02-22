from django.contrib import admin

from api.models import Project

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['date', 'name', 'description', 'text', 'image']


admin.site.register(Project, ProjectAdmin)

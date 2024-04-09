# admin.py

from django.contrib import admin
from .models import Project, Icon

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']  # Add other fields as needed

class IconAdmin(admin.ModelAdmin):
    list_display = ['name']  # Add other fields as needed

admin.site.register(Project, ProjectAdmin)
admin.site.register(Icon, IconAdmin)

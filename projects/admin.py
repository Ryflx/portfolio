from django.contrib import admin
from .models import Project

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'order', 'created_at')
    list_filter = ('technology',)
    search_fields = ('title', 'description', 'technology')
    ordering = ('order', '-created_at')

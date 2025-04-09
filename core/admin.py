from django.contrib import admin
from .models import Skill, Education, Experience, Contact

# Register your models here.

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    search_fields = ('name', 'description')
    ordering = ('order',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'university', 'start_date', 'end_date')
    search_fields = ('degree', 'university', 'field_of_study')
    list_filter = ('university',)
    ordering = ('-end_date', '-start_date')
    date_hierarchy = 'start_date'

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'location', 'start_date', 'end_date')
    search_fields = ('position', 'company', 'description')
    list_filter = ('company',)
    ordering = ('-end_date', '-start_date')
    date_hierarchy = 'start_date'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

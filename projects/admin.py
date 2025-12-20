from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'created_at']
    list_filter = ['created_at', 'skills']
    search_fields = ['title', 'description']
    list_editable = ['order']
    filter_horizontal = ['skills']  # Skill seçimi için daha iyi UI
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('title', 'description', 'order')
        }),
        ('Medya', {
            'fields': ('image',)
        }),
        ('Linkler', {
            'fields': ('url', 'github_url')
        }),
        ('Teknolojiler', {
            'fields': ('skills',)
        }),
    )


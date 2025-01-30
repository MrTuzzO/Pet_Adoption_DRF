from django.contrib import admin
from .models import Bird

@admin.register(Bird)
class BirdAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'size')
    list_filter = ('size', 'diet')
    search_fields = ('name', 'species', 'description')
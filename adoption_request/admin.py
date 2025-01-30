from django.contrib import admin
from .models import AdoptionRequest


@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    # List view fields
    list_display = ('id', 'pet_name', 'requester_name', 'status', 'date_requested', 'use_default_info')
    list_filter = ('status', 'date_requested')  # Filters for quick navigation
    search_fields = ('pet__name', 'requester__username', 'requester__email')  # Search bar for pet name or requester details
    ordering = ('-date_requested',)  # Order by most recent requests

    def pet_name(self, obj):
        return obj.pet.name
    pet_name.short_description = 'Pet'

    def requester_name(self, obj):
        return obj.requester.username
    requester_name.short_description = 'Requester'

    # Add inline editing for the status field
    list_editable = ('status',)

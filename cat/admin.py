from django.contrib import admin
from .models import Cat, CatColor


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'food_habit', 'is_potty_trained', 'description', 'display_colors')
    search_fields = ('name', 'food_habit', 'description')
    list_filter = ('is_potty_trained',)
    filter_horizontal = ('colors',)
    readonly_fields = ('id',)

    # Helper to display colors in the admin panel
    def display_colors(self, obj):
        return ", ".join([color.name for color in obj.colors.all()])
    display_colors.short_description = "Colors"


admin.site.register(CatColor)
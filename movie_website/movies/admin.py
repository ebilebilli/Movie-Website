from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'release_date', 'duration', 'rating')
    list_filter = ('release_date', 'categories', 'director', 'actors')
    search_fields = (
        'title',
        'description',
        'director__name',
        'actors__name',
        'categories__title',
    )
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('categories', 'actors')
    readonly_fields = ('created_at', 'updated_at')

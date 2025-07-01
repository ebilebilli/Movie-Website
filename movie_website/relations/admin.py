from django.contrib import admin

from relations.models.category import Category
from relations.models.director import Director
from relations.models.actor import Actor
from relations.models.release_date import ReleaseDate


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


from django.contrib import admin
from .models import ReleaseDate


@admin.register(ReleaseDate)
class ReleaseDateAdmin(admin.ModelAdmin):
    list_display = ('id', 'year')
    search_fields = ('year',)
    ordering = ('-year',)
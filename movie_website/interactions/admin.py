from django.contrib import admin
from interactions.models.comment import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'movie', 'parent', 'short_text', 'created_at')
    list_filter = ('movie', 'user', 'created_at')
    search_fields = ('text', 'user__username', 'movie__title')
    autocomplete_fields = ('user', 'movie', 'parent')
    readonly_fields = ('created_at', 'updated_at')

    def short_text(self, obj):
        return (obj.text[:50] + '...') if len(obj.text) > 50 else obj.text
    short_text.short_description = 'Text'

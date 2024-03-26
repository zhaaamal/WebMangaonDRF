from django.contrib import admin
from .models import Manga, Comment, Author, Category, Genre


class MangaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_date', 'updated_date', 'completed', 'img_thumbnail')
    list_filter = ('author', 'category', 'completed')
    search_fields = ('title', 'author__name', 'category__title')
    readonly_fields = ('created_date', 'updated_date', 'img_thumbnail')

    def img_thumbnail(self, obj):
        return obj.img.url if obj.img else None
    img_thumbnail.short_description = 'Thumbnail'
    img_thumbnail.allow_tags = True


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'manga', 'created_date', 'updated_date')
    list_filter = ('user', 'manga')
    search_fields = ('user__username', 'manga__title')


admin.site.register(Manga, MangaAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Genre)

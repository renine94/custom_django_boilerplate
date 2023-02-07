from django.contrib import admin

from app.boards.models import Article, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display_links = ['user']
    list_display = ['pk', 'user', 'content', 'created_at', 'updated_at']
    readonly_fields = ['like_count']
    ordering = ['-created_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'content', 'created_at', 'updated_at')

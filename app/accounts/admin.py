from django.contrib import admin

from app.accounts.models import User


@admin.register(User)
class ArticleAdmin(admin.ModelAdmin):
    list_display_links = ['email']
    list_display = ['pk', 'email', 'name', 'nickname', 'created_at', 'updated_at', 'is_active']
    ordering = ['-created_at']

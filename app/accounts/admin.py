from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from app.accounts.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display_links = ['username']
    readonly_fields = ['id']
    ordering = ['-date_joined']

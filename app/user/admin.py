"""User models admin."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User, Profile


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_client')
    list_filter = ('is_client', 'is_staff')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('user', 'movies_create', 'movies_recomment')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')


admin.site.register(User, CustomUserAdmin)

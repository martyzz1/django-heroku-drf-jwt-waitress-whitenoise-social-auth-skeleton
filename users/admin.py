from django.contrib import admin
from custom_user.admin import EmailUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(EmailUserAdmin):
    """
    You can customize the interface of your model here.
    """
    list_display = ('email', 'first_name', 'last_name', 'user_type', 'is_staff')
    list_filter = ('user_type', 'is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name', 'user_type')
    filter_horizontal = ('groups', 'user_permissions',)

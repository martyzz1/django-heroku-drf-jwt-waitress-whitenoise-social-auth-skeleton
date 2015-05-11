from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from custom_user.admin import EmailUserAdmin
from .models import User
from .forms import EmailUserCreationForm, EmailUserChangeForm
from django.utils.translation import ugettext_lazy as _


"""
Override the add- and change-form in the admin, to hide the username.
"""


@admin.register(User)
class UserAdmin(UserAdmin):
    """
    You can customize the interface of your model here.
    """

    fieldsets = (
        (None, {'fields': ('email', 'password', 'user_type')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = ((
        None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }
    ),
    )

    list_display = ('email', 'first_name', 'last_name', 'user_type', 'is_staff')
    list_filter = ('user_type', 'is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name', 'user_type')
    filter_horizontal = ('groups', 'user_permissions',)
    add_form = EmailUserCreationForm
    form = EmailUserChangeForm


# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)


def __email_unicode__(self):
    return self.email

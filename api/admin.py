from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, UserProfile, Car

admin.site.register(Car)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    exclude = ('first_name', 'last_name', )
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Personal info'), {'fields': ('name', 'siape')}),
        (_('Permissions'), {'fields': (
            'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'name', 'is_active', 'is_superuser')
    # list_display = ('email', 'name', 'is_active', 'is_superuser', 'is_servidor', 'is_diretor', 'is_gestor')
    search_fields = ('email', 'name')
    ordering = ('email',)
    inlines = (UserProfileInline, )
    list_filter = ('is_active', 'is_superuser')

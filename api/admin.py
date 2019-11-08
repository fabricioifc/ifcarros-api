from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, UserProfile, Car, Solicitation, Passenger

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    pass

@admin.register(Solicitation)
class SolicitationAdmin(admin.ModelAdmin):
    readonly_fields = ['user']
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(SolicitationAdmin, self).save_model(request, obj, form, change)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    readonly_fields = ['user']
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(CarAdmin, self).save_model(request, obj, form, change)
    
    # fieldsets = (
    #     (None, {'fields': ('marca', 'modelo', 'km', 'ano', 'descricao', 'imagem')}),
    # )

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(CarAdmin, self).get_form(request, obj, **kwargs)
    #     form.base_fields['user'].initial = request.user
    #     return form

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'user':
    #         kwargs['queryset'] = User.objects.filter(id=request.user.id)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    exclude = ('first_name', 'last_name', )
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Personal info'), {'fields': ('name', 'siape', 'funcao', 'cpf')}),
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

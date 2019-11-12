from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.urls import reverse

from .models import *

@admin.register(Autorization)
class AutorizationAdmin(admin.ModelAdmin):
    readonly_fields = ('user', )
    list_display = ['__str__', 'get_user_sol', 'get_dthr_sol', 'dthrautorizacao', 'get_user_aut', 'status']
    ordering = ['-dthrautorizacao']

    def get_user_aut(self, obj):
        return obj.user.name
    def get_user_sol(self, obj):
        return obj.solicitation.user.name
    def get_dthr_sol(self, obj):
        return obj.solicitation.dthrrequisicao
    get_user_sol.short_description = 'Solicitante'
    # get_user_aut.short_description = 'Autorizador'
    get_dthr_sol.short_description = 'Data Solicitação'

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(AutorizationAdmin, self).save_model(request, obj, form, change)


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    pass

@admin.register(Solicitation)
class SolicitationAdmin(admin.ModelAdmin):
    readonly_fields = ['user', 'get_status_aut']
    list_display = ['__str__', 'get_user_sol', 'dthrrequisicao', 'get_user_aut', 'get_dhtr_aut', 'get_status_aut']
    # ordering = ['-dthrrequisicao', 'autorization__status']
    list_filter = ('dthrrequisicao', 'autorization__user__name', 'autorization__status' )
    # actions = ['efetuar_autorizacao']
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(SolicitationAdmin, self).save_model(request, obj, form, change)

    def get_user_aut(self, obj):
        return obj.autorization.user.name
    def get_dhtr_aut(self, obj):
        return obj.autorization.dthrautorizacao
    def get_status_aut(self, obj):
        return obj.autorization.STATUS[obj.autorization.status]
    def get_user_sol(self, obj):
        return obj.user.name
    # def my_link(self, obj):
    #     # info = (obj._meta.app_label, obj._meta.model_name)
    #     info = (obj._meta.app_label, 'autorization')
    #     admin_url = reverse('admin:%s_%s_changelist' % info)
    #     return admin_url

    get_user_sol.short_description = 'Solicitado por'
    get_user_aut.short_description = 'Autorizado por'
    get_dhtr_aut.short_description = 'Autorizador em'
    get_status_aut.short_description = 'Status'

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

from ..validators import validate_CPF
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(
        blank=False, null=False, max_length=20, unique=True)
    name = models.CharField(blank=False, null=False, max_length=300, verbose_name='Nome')
    email = models.EmailField(_('email address'), unique=True)
    siape = models.PositiveIntegerField(blank=True, null=True)
    funcao = models.CharField(blank=True, null=True, max_length=45)
    cpf = models.CharField(unique=True, blank=True, null=True, max_length=11, validators=[validate_CPF])
    # is_servidor = models.BooleanField(
    #     'Servidor', default=True, help_text='Indica que este usuário é Servidor do campus')
    # is_gestor = models.BooleanField(
    #     'Gestor', default=False, help_text='Indica que este usuário é Gestor da frota')
    # is_diretor = models.BooleanField(
    #     'Diretor', default=False, help_text='Indica que este usuário é Diretor do Campus')
    is_superuser = models.BooleanField(
        'Admin', default=False, help_text='Indica que este usuário é Administrador')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    dtnascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=60)
    cep = models.CharField(max_length=8)
    avatar = models.ImageField(upload_to='uploads', blank=True)

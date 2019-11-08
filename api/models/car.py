import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.validators import MaxValueValidator
from .geral import Geral
from .user import User


# def year_choices():
#     return [(r, r) for r in range(1984, datetime.date.today().year+1)]


class Car(Geral):
    """Model definition for Car."""

    marca = models.CharField(max_length=45, blank=False, null=False)
    modelo = models.CharField(max_length=45)
    ano = models.PositiveIntegerField(blank=False, null=False, validators=[
                                      MaxValueValidator(2100)])
    km = models.PositiveIntegerField()
    descricao = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    imagem = models.ImageField(_("Foto do Veículo"), upload_to='uploads/car', height_field=None, width_field=None, max_length=None, blank=True, null=True)

    class Meta:
        """Meta definition for Car."""

        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        """Unicode representation of Car."""
        return self.marca + ' ' + self.modelo

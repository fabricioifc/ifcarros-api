import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.validators import MaxValueValidator
from .geral import Geral
from .user import User

class Passenger(Geral):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Solicitation(Geral):
    """Model definition for Solicitation."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    finalidade = models.TextField(blank=False)
    dthrsaida = models.DateTimeField()
    dthrretorno = models.DateTimeField()
    dthrrequisicao = models.DateTimeField(editable=False, default=timezone.now)
    passageiros = models.ManyToManyField(Passenger)

    # class Meta:
    #     """Meta definition for Car."""

    #     verbose_name = 'Solicitation'
    #     verbose_name_plural = 'Solicitations'

    # def __str__(self):
    #     """Unicode representation of Car."""
    #     return self

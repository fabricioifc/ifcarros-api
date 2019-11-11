import datetime
from model_utils import Choices
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

    class Meta:
        verbose_name = "Passageiro"
        verbose_name_plural = "Passageiros"

    def __str__(self):
        return self.nome

class Solicitation(Geral):
    """Model definition for Solicitation."""
    STATUS = Choices(('solicitado', _('Solicitado')), ('autorizado', _('Autorizado')), ('nao_autorizado', _('Não Autorizado')))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    finalidade = models.TextField(blank=False)
    dthrsaida = models.DateTimeField('Data da Saída')
    dthrretorno = models.DateTimeField('Data do Retorno')
    dthrrequisicao = models.DateTimeField('Solicitado em', editable=False, default=timezone.now)
    passageiros = models.ManyToManyField(Passenger, verbose_name='Passageiros',)
    status = models.CharField('Status',choices=STATUS, max_length=30, blank=True, null=True)
    # user_autorizador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, blank=True, null=True)
    # dthranalise = models.DateTimeField(editable=False, default=timezone.now)

    class Meta:
        verbose_name = 'Solicitação'
        verbose_name_plural = 'Solicitações'
        ordering = ['-status']

    def __str__(self):
        numero = str(self.id).zfill(3)
        return str('Solicitação n°') + numero
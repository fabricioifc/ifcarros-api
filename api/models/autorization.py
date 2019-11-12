import datetime
from model_utils import Choices
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.validators import MaxValueValidator
from .geral import Geral
from .solicitation import Solicitation

class Autorization(Geral):
    """Model definition for Autorization."""
    STATUS = Choices(('analise', _('Em Análise')), ('autorizado', _('Autorizado')), ('nao_autorizado', _('Não Autorizado')))

    # solicitation = models.ForeignKey(Solicitation, related_name='Solicitation', on_delete=models.DO_NOTHING)
    solicitation = models.OneToOneField(Solicitation, on_delete=models.CASCADE, related_name="autorization")
    motivo = models.TextField(blank=False)
    dthrautorizacao = models.DateTimeField(editable=False, default=timezone.now, verbose_name='Autorizado em')
    status = models.CharField(choices=STATUS, default=STATUS.analise, max_length=30, verbose_name='Status')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, verbose_name='Autorizado por')

    class Meta:
        verbose_name = 'Autorização'
        verbose_name_plural = 'Autorizações'

    def __str__(self):
        numero = str(self.solicitation.id).zfill(3)
        return str('Solicitação n°') + numero

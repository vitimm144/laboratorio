from django.db import models
from django.core.urlresolvers import reverse


class Posto(models.Model):

    nome_posto = models.CharField(max_length=200, verbose_name='Posto de Coleta')
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    prefixo = models.CharField(max_length=10, verbose_name='Prefixo')

    def get_absolute_url(self):
        return reverse('posto_edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('posto_delete', kwargs={'pk': self.pk})


from django.db import models

class Posto(models.Model):

    nome_posto = models.CharField(max_length=200, verbose_name='Posto de Coleta')
    endereco = models.CharField(max_length=200, verbose_name='Endereco')
    prefixo = models.CharField(max_length=10, verbose_name='prefixo')


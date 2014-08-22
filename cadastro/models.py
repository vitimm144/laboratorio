from django.db import models


class Paciente(models.Model):

    numero_paciente = models.CharField(verbose_name='Numero do Paciente')
    data_registro = models.DateField(verbose_name='Data de Registro')
    nome = models.CharField(max_length=200, verbose_name='Nome')
    GENDER_CHOICES = (
        (u'M', u'Masculino'),
        (u'F', u'Feminino'),
    )
    sexo = models.CharField(max_length=2, choices=GENDER_CHOICES, verbose_name='Sexo')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    nome_mae = models.CharField(max_length=200, verbose_name='Nome da Mãe')
    cep = models.ForeignKey()
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    numero = models.CharField(max_length=20, verbose_name='numero')
    complemento = models.CharField(max_length=100, verbose_name='Compl.')
    bairro = models.CharField(max_length=50, verbUose_name='Bairro')
    Cidade = models.CharField(max_length=100, verbose_name='Cidade')
    UF = models.BRStatefield(verbose_name='2')
    rg = models.CharField(max_length=12, verbose_name='RG')
    CPF = models.CharField(max_length=12, verbose_name='CPF')
    telefone = models.CharField(max_length='10', verbose_name='Telefone')
    celular = models.CharField(max_length='11', verbose_name='Celular')
    SUS_CHOICES = (
        (u'Sim', u'SIM')
        (u'Nao', u'NAO')

    )
convenio_sus = models.CharField(max_length='10', choices=SUS_CHOICES, verbose_name='Conveniado SUS?')
numero_sus = models.CharField(max_length=12, verbose_name='Numero SUS')
email = models.CharField(max_length=20, verbose_name='E-mail')
informacao_menor = models.CharField(max_length=200, verbose_name='Informações do Menor')

class medico (models.Model):
    crm = models.CharField(max_length=10, verbose_name='CRM')
    nome_medico = models.CharField(max_length=200, verbose_name='Nome:')

class tabela_exame (models.Model):
    nome_tabela = models.CharField(max_length=200, verbose_name='Nome da Tabela de Exames')
    codigo_exame = models.CharField(max_length=10, verbose_name='Código do Exame')
    nome_exame = models.CharField(max_length=100, verbose_name='Nome do Exame')
    ch = models.CharField(max_length=5, verbose_name='Valor de CH')

class convenio (models.Model):
    nome_convenio = models.CharField(max_length=100, verbose_name='Nome do Convenio')
    tipo_tabela = models.CharField(verbose_name='Tipo de Tabela')
    precificacao = models.CharField(max_length=10, verbose_name='Precificação')

# Create your models here.

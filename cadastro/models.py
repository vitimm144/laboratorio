from django.db import models


class Paciente(models.Model):

    numero_paciente = models.IntegerField(verbose_name='Numero do Paciente', unique=True, auto_created=True)
    data_registro = models.DateField(verbose_name='Data de Registro', auto_now=True)
    nome = models.CharField(max_length=200, verbose_name='Nome')
    GENDER_CHOICES = (
        (u'M', u'Masculino'),
        (u'F', u'Feminino'),
    )
    sexo = models.CharField(max_length=2, choices=GENDER_CHOICES, verbose_name='Sexo')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    nome_mae = models.CharField(max_length=200, verbose_name='Nome da Mãe')
    cep = models.CharField(max_length=10, null=True, verbose_name='CEP')
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    numero = models.CharField(max_length=20, verbose_name='numero')
    complemento = models.CharField(max_length=100, verbose_name='Compl.')
    bairro = models.CharField(max_length=50, verbose_name='Bairro')
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    uf = models.BRStatefield(verbose_name='UF')
    rg = models.CharField(max_length=12, verbose_name='RG')
    cpf = models.CharField(max_length=12, verbose_name='CPF')
    telefone = models.CharField(max_length='10', verbose_name='Telefone')
    celular = models.CharField(max_length='11', verbose_name='Celular')
    SUS_CHOICES = (
        (u'S', u'SIM'),
        (u'N', u'NÃO'),
    )
    convenio_sus = models.CharField(max_length='10', choices=SUS_CHOICES, verbose_name='Conveniado SUS?', null=True)
    numero_sus = models.CharField(max_length=12, verbose_name='Numero SUS', null=True)
    email = models.CharField(max_length=20, verbose_name='E-mail', null=True)
    informacao_menor = models.CharField(max_length=200, verbose_name='Informações do Menor', null=True)


class Medico (models.Model):
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

from django.db import models
from django.core.urlresolvers import reverse
import uuid


class Paciente(models.Model):

    numero_paciente = models.PositiveIntegerField(
        verbose_name='Numero do Paciente',
        unique=True,
        primary_key=True,
        auto_created=True
    )
    data_registro = models.DateField(verbose_name='Data de Registro', auto_now=True)
    nome = models.CharField(max_length=200, verbose_name='Nome')
    GENDER_CHOICES = (
        (u'M', u'Masculino'),
        (u'F', u'Feminino'),
    )
    sexo = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name='Sexo')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    nome_mae = models.CharField(max_length=200, verbose_name='Nome da Mãe')
    #TODO: pesquisar preenchimento automatico pelo site dos correios
    cep = models.CharField(max_length=10, null=True, verbose_name='CEP')
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    numero = models.CharField(max_length=20, verbose_name='numero')
    complemento = models.CharField(max_length=100, verbose_name='Compl.')
    bairro = models.CharField(max_length=50, verbose_name='Bairro')
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    #TODO: rever uso de UF pois quase 100% dos pacientes atendidos são do Estado
    uf = models.CharField(max_length=10, verbose_name='UF', default='RJ')
    rg = models.CharField(max_length=12, verbose_name='RG')
    cpf = models.CharField(max_length=12, verbose_name='CPF')
    telefone = models.CharField(max_length=10, verbose_name='Telefone')
    celular = models.CharField(max_length=11, verbose_name='Celular')
    SUS_CHOICES = (
        (u'S', u'SIM'),
        (u'N', u'NÃO'),
    )
    convenio_sus = models.CharField(max_length=10, choices=SUS_CHOICES, verbose_name='Conveniado SUS?', null=True)
    numero_sus = models.CharField(max_length=12, verbose_name='Numero SUS', null=True, blank=True)
    email = models.EmailField(verbose_name='E-mail', null=True, max_length=100)
    informacao_menor = models.CharField(max_length=200, verbose_name='Informações do Menor', null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['numero_paciente']

    def get_absolute_url(self):
        return reverse('paciente_edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('paciente_delete', kwargs={'pk': self.pk})


class Medico (models.Model):
    crm = models.CharField(max_length=10, verbose_name='CRM')
    nome_medico = models.CharField(max_length=200, verbose_name='Nome:')

    def __str__(self):
        return self.nome_medico

    def get_absolute_url(self):
        return reverse('medico_edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('medico_delete', kwargs={'pk': self.pk})


class Exame(models.Model):
    codigo_exame = models.CharField(max_length=10, verbose_name='Código do Exame')
    nome_exame = models.CharField(max_length=100, verbose_name='Nome do Exame')
    ch = models.CharField(max_length=5, verbose_name='Valor de CH')

    def __str__(self):
        return self.nome_exame

    def get_absolute_url(self):
        return reverse('exame_edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('exame_delete', kwargs={'pk': self.pk})


class Tabela_exame (models.Model):
    nome_tabela = models.CharField(max_length=200, verbose_name='Nome da Tabela de Exames')
    exames = models.ManyToManyField('Exame', related_name='exames')

    def __str__(self):
        return self.nome_tabela

    def get_absolute_url(self):
        return reverse('tabela_exame_edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('tabela_exame_delete', kwargs={'pk': self.pk})


class Convenio (models.Model):
    nome_convenio = models.CharField(max_length=100, verbose_name='Nome do Convenio')
    tipo_tabela = models.ForeignKey('Tabela_exame', verbose_name='Tipo de Tabela')
    precificacao = models.CharField(max_length=10, verbose_name='Precificação')

    def __str__(self):
        return self.nome_convenio

    def get_absolute_url(self):
        return reverse('convenio_edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('convenio_delete', kwargs={'pk': self.pk})


class Atendimento(models.Model):

    data_coleta = models.DateTimeField(auto_now_add=True)
    #TODO: O codigo do atendimento obedece ao local de coleta
    codigo = models.UUIDField(unique=True, default=uuid.uuid4)
    paciente = models.ForeignKey('Paciente', verbose_name='Paciente')
    medico = models.ForeignKey('Medico', verbose_name='Médico solicitante')
    atendimento_exames = models.ManyToManyField('Atendimento_exame', related_name='atendimento_exames')
    data_resultado = models.DateField()
    observacao = models.TextField()
    peso = models.CharField(max_length=10, verbose_name='Peso')
    altura = models.CharField(max_length=4, verbose_name='Altura')
    dum = models.CharField(max_length=10, verbose_name='DUM')
    # valor_total = models.DecimalField(verbose_name='Valor total')
    # valor_pago = models.DecimalField(verbose_name='Valor pago')
    # valor_devido = models.DecimalField(verbose_name='Valor devido')
    medicamentos = models.TextField(verbose_name='Medicamentos', null=True)
    #TODO:criar uma senha randomica para acesso do paciente para os laudos via internet
    senha = models.CharField(max_length=8, verbose_name='Senha internet')

    def get_absolute_url(self):
        return reverse('atendimento_edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('atendimento_delete', kwargs={'pk': self.pk})


class Atendimento_exame(models.Model):
    convenios = models.ForeignKey('Convenio')
    exames = models.ManyToManyField('Exame')

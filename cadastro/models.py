from django.db import models
from django.core.urlresolvers import reverse


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
    #TODO: pesquisar preenchimento automatico pelo site dos correios
    cep = models.CharField(max_length=10, null=True, verbose_name='CEP')
    endereco = models.CharField(max_length=200, verbose_name='Endereço')
    numero = models.CharField(max_length=20, verbose_name='numero')
    complemento = models.CharField(max_length=100, verbose_name='Compl.')
    bairro = models.CharField(max_length=50, verbose_name='Bairro')
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    #TODO: rever uso de UF pois quase 100% dos pacientes atendidos são do Estado
    uf = models.CharField(max_length=2, verbose_name='UF', default='RJ')
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

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['numero_paciente']


class Medico (models.Model):
    crm = models.CharField(max_length=10, verbose_name='CRM')
    nome_medico = models.CharField(max_length=200, verbose_name='Nome:')

    def get_absolute_url(self):
        return reverse('medico_edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('medico_delete', kwargs={'pk': self.pk})


class Exame(models.Model):
    codigo_exame = models.CharField(max_length=10, verbose_name='Código do Exame')
    nome_exame = models.CharField(max_length=100, verbose_name='Nome do Exame')
    ch = models.CharField(max_length=5, verbose_name='Valor de CH')



class Tabela_exame (models.Model):
    nome_tabela = models.CharField(max_length=200, verbose_name='Nome da Tabela de Exames')
    exames = models.ManyToManyField('Exame', related_name='exames')


class Convenio (models.Model):
    nome_convenio = models.CharField(max_length=100, verbose_name='Nome do Convenio')
    tipo_tabela = models.ForeignKey('Tabela_exame', verbose_name='Tipo de Tabela')
    precificacao = models.CharField(max_length=10, verbose_name='Precificação')


class Atendimento(models.Model):

    data_coleta = models.DateTimeField(auto_now_add=True)
    #TODO: O codigo do atendimento obedece ao local de coleta
    codigo = models.IntegerField(verbose_name='Codigo do atendimento', unique=True, auto_created=True)
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


class Atendimento_exame(models.Model):
    convenios = models.ForeignKey('Convenio')
    exames = models.ManyToManyField('Exame')

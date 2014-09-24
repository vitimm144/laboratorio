from django.forms import ModelForm
from django import forms
from django.core import validators
from .models import Paciente, Medico, Exame, Tabela_exame, Convenio, Atendimento


class PacienteForm(ModelForm):

    # numero_paciente = forms.IntegerField()
    # data_nascimento = forms.DateField()

    class Meta:
        model = Paciente
        # fields = ['numero_paciente', 'data_registro', 'nome', 'sexo', 'data_nascimento'
        #           'nome_mae', 'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade'
        #           'uf', 'rg', 'cpf', 'telefone', 'celular', 'convenio_sus', 'numero_sus', 'email',
        #           'informacao_menor']
        fields = '__all__'

    # def clean_numero_paciente(self):
    #     numero_paciente = self.cleaned_data['numero_paciente']
    #     return int(numero_paciente)
    #
    # def full_clean(self):
    #     import ipdb; ipdb.set_trace()
    #     return super(PacienteForm, self).full_clean()


class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'


class ExameForm(ModelForm):
    class Meta:
        model = Exame
        fields = '__all__'


class TexameForm(ModelForm):
    class Meta:
        model = Tabela_exame
        fields = '__all__'


class ConvenioForm(ModelForm):
    class Meta:
        model = Convenio
        fields = '__all__'


class AtendimentoForm(ModelForm):
    class Meta:
        model = Atendimento
        fields = '__all__'
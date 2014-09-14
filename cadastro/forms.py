from django.forms import ModelForm
from .models import Paciente, Medico, Exame, Tabela_exame, Convenio, Atendimento


class PacienteForm(ModelForm):

    class Meta:
        model = Paciente
         # def clean_rg(self):


class MedicoForm(ModelForm):
    class Meta:
        model = Medico


class ExameForm(ModelForm):
    class Meta:
        model = Exame


class TexameForm(ModelForm):
    class Meta:
        model = Tabela_exame


class ConvenioForm(ModelForm):
    class Meta:
        model = Convenio


class AtendimentoForm(ModelForm):
    class Meta:
        model = Atendimento

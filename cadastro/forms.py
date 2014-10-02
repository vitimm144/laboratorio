from django.forms import ModelForm
from .models import Paciente, Medico, Exame, Tabela_exame, Convenio, Atendimento


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'


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
from django.forms import ModelForm
from .models import Paciente
from .models import Medico
from .models import Exame
from .models import Tabela_exame
from .models import Convenio
from .models import Atendimento

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente

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
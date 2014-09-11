from django.forms import ModelForm
from .models import Paciente
from .models import Medico
from .models import Exame

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente

class MedicoForm(ModelForm):
    class Meta:
        model = Medico

class ExameForm(ModelForm):
    class Meta:
        model = Exame
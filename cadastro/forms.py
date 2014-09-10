from django.forms import ModelForm
from .models import Paciente
from .models import Medico


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente

class MedicoForm(ModelForm):
    class Meta:
        model = Medico
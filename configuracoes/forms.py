from django.forms import ModelForm
from .models import Posto

class PostoForm(ModelForm)
    class Meta:
        model = Posto
        fieods = '__all__'



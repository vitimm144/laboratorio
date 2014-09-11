from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView
from .models import Paciente
from .forms import PacienteForm
from .models import Medico
from .forms import MedicoForm
from .models import Exame
from .forms import ExameForm
from .models import Tabela_exame
from .forms import TexameForm
from .models import Convenio
from .forms import ConvenioForm



@login_required(login_url='/login/')
def home(request):
    return render(request, 'index.html')


class CadastroPacienteView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente_form.html'

    # def post(self, request, *args, **kwargs):
    #     import ipdb; ipdb.set_trace()
    #     return super(CadastroPacienteView, self).post(request, *args, **kwargs)

class PacienteListView(ListView):
    model = Paciente

class CadastroMedicoView(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico_form.html'

    #def post(self, request, *args, **kwargs);
    #   import ipdb; ipdb.set_trace()
    #   return super (CadastroMedicoView, self).post(request, *args, **kwargs)

class MedicoListView(ListView):
    model = Medico

class CadastroExameView(CreateView):
    model = Exame
    form_class = ExameForm
    template_name = "exame.html"

class ExameListView(ListView):
    model = Exame

class CadastroTexameView(CreateView):
    model = Tabela_exame
    form_class = TexameForm
    template_name = 'tabela_exames.html'

class TexameListView(ListView):
    model = Tabela_exame

class CadastroConvenioView(CreateView):
    model = Convenio
    form_class = ConvenioForm
    template_name = 'convenio_form.html'

class ConvenioListView(ListView):
    model = Convenio
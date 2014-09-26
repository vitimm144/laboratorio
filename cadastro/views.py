from django.shortcuts import render
from django.utils import timezone
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Paciente, Medico, Exame, Tabela_exame, Convenio, Atendimento
from .forms import PacienteForm, MedicoForm, ExameForm, TexameForm, ConvenioForm, AtendimentoForm


@login_required(login_url='/login/')
def home(request):
    return render(request, 'index.html')

#############################
# Views de Paciente
#############################

class PacienteCreate(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente_form.html'

    def get_success_url(self):
        return reverse('paciente_list')

    # def post(self, request, *args, **kwargs):
    #     paciente = request.POST.dict()
    #     paciente['numero_paciente'] = int(paciente.get('numero_paciente'))
    #
    #     # form = PacienteForm(paciente)
    #     # # import ipdb; ipdb.set_trace()
    #     # form.full_clean()
    #     # form.clean()
    #     if form.is_valid():
    #         form.save()
    #         return super(CadastroPacienteView, self).post(request, *args, **kwargs)

        # return

class PacienteUpdate(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente_form.html'

    def get_success_url(self):
        return reverse('paciente_list')


class PacienteDelete(DeleteView):
    model = Paciente
    # template_name_suffix = 'templates/'
    template_name = 'paciente_confirm_delete.html'

    def get_success_url(self):
        return reverse('paciente_list')


class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente_list.html'

###############################################

#############################
# Views de Medico
#############################
class MedicoCreate(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico_form.html'

    def get_success_url(self):
        return reverse('medico_list')


class MedicoUpdate(UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico_form.html'

    def get_success_url(self):
        return reverse('medico_list')


class MedicoDelete(DeleteView):
    model = Medico
    # template_name_suffix = 'templates/'
    template_name = 'medico_confirm_delete.html'

    def get_success_url(self):
        return reverse('medico_list')


class MedicoListView(ListView):
    model = Medico
    template_name = 'medico_list.html'

##############################

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


class CadastroAtendimentoView(CreateView):
    model = Atendimento
    form_class = AtendimentoForm
    template_name = 'atendimento_form.html'

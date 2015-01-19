from django.shortcuts import render
from django.utils import timezone
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormView
from .models import Paciente, Medico, Exame, Tabela_exame, Convenio, Atendimento
from .forms import PacienteForm, MedicoForm, ExameForm, TexameForm, ConvenioForm, AtendimentoForm


class AjaxTemplateMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)

        if request.is_ajax():
            self.template_name = self.ajax_template_name

        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)


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


#############################
# Views de Exame
#############################
class ExameCreate(CreateView):
    model = Exame
    form_class = ExameForm
    template_name = 'exame_form.html'

    def get_success_url(self):
        return reverse('exame_list')


class ExameUpdate(UpdateView):
    model = Exame
    form_class = ExameForm
    template_name = 'exame_form.html'

    def get_success_url(self):
        return reverse('exame_list')


class ExameDelete(DeleteView):
    model = Exame
    # template_name_suffix = 'templates/'
    template_name = 'exame_confirm_delete.html'

    def get_success_url(self):
        return reverse('exame_list')


class ExameListView(ListView):
    model = Exame
    template_name = 'exame_list.html'

######################################


class TexameCreate(CreateView):
    model = Tabela_exame
    form_class = TexameForm
    template_name = 'tabela_exame_form.html'

    def get_success_url(self):
        return reverse('tabela_exame_list')


class TexameUpdate(UpdateView):
    model = Tabela_exame
    form_class = TexameForm
    template_name = 'tabela_exame_form.html'

    def get_success_url(self):
        return reverse('tabela_exame_list')


class TexameDelete(DeleteView):
    model = Tabela_exame
    template_name = 'tabela_exame_confirm_delete.html'

    def get_success_url(self):
        return reverse('tabela_exame_list')


class TexameListView(ListView):
    model = Tabela_exame
    template_name = 'tabela_exame_list.html'

#########


class ConvenioCreate(CreateView):
    model = Convenio
    form_class = ConvenioForm
    template_name = 'convenio_form.html'

    def get_success_url(self):
        return reverse('convenio_list')


class ConvenioUpdate(UpdateView):
    model = Convenio
    form_class = ConvenioForm
    template_name = 'convenio_form.html'

    def get_success_url(self):
        return reverse('convenio_list')


class ConvenioDelete(DeleteView):
    model = Convenio
    template_name = 'convenio_confirm_delete.html'

    def get_success_url(self):
        return reverse('convenio_list')


class ConvenioListView(ListView):
    model = Convenio
    template_name = 'convenio_list.html'


#############################
# Views de Atendimento
#############################
from django.core.urlresolvers import reverse_lazy


class PacienteView(FormView):
    template_name = 'paciente_form_inner.html'
    form_class = PacienteForm
    success_url = reverse_lazy('atendimento_new')
    # success_message = "Way to go!"


class AtendimentoCreate(CreateView):
    model = Atendimento
    form_class = AtendimentoForm
    template_name = 'atendimento_form.html'

    def get_success_url(self):
        return reverse('atendimento_list')


class AtendimentoUpdate(UpdateView):
    model = Atendimento
    form_class = AtendimentoForm
    template_name = 'atendimento_form.html'

    def get_success_url(self):
        return reverse('atendimento_list')


class AtendimentoDelete(DeleteView):
    model = Atendimento
    # template_name_suffix = 'templates/'
    template_name = 'atendimento_confirm_delete.html'

    def get_success_url(self):
        return reverse('atendimento_list')


class AtendimentoListView(ListView):
    model = Atendimento
    template_name = 'atendimento_list.html'

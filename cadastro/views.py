from django.shortcuts import render
from django.utils import timezone
from django.core.urlresolvers import reverse
from login.views import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
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
class PacienteCreate(LoginRequiredMixin, CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente_form.html'

    def get_success_url(self):
        return reverse('paciente_list')


class PacienteUpdate(LoginRequiredMixin, UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente_form.html'

    def get_success_url(self):
        return reverse('paciente_list')


class PacienteDelete(LoginRequiredMixin, DeleteView):
    model = Paciente
    # template_name_suffix = 'templates/'
    template_name = 'paciente_confirm_delete.html'

    def get_success_url(self):
        return reverse('paciente_list')


class PacienteListView(LoginRequiredMixin, ListView):
    model = Paciente
    template_name = 'paciente_list.html'

###############################################


#############################
# Views de Medico
#############################
class MedicoCreate(LoginRequiredMixin, CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico_form.html'

    def get_success_url(self):
        return reverse('medico_list')


class MedicoUpdate(LoginRequiredMixin, UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico_form.html'

    def get_success_url(self):
        return reverse('medico_list')


class MedicoDelete(LoginRequiredMixin, DeleteView):
    model = Medico
    # template_name_suffix = 'templates/'
    template_name = 'medico_confirm_delete.html'

    def get_success_url(self):
        return reverse('medico_list')


class MedicoListView(LoginRequiredMixin, ListView):
    model = Medico
    template_name = 'medico_list.html'

##############################


#############################
# Views de Exame
#############################
class ExameCreate(LoginRequiredMixin, CreateView):
    model = Exame
    form_class = ExameForm
    template_name = 'exame_form.html'

    def get_success_url(self):
        return reverse('exame_list')


class ExameUpdate(LoginRequiredMixin, UpdateView):
    model = Exame
    form_class = ExameForm
    template_name = 'exame_form.html'

    def get_success_url(self):
        return reverse('exame_list')


class ExameDelete(LoginRequiredMixin, DeleteView):
    model = Exame
    # template_name_suffix = 'templates/'
    template_name = 'exame_confirm_delete.html'

    def get_success_url(self):
        return reverse('exame_list')


class ExameListView(LoginRequiredMixin, ListView):
    model = Exame
    template_name = 'exame_list.html'

######################################


class TexameCreate(LoginRequiredMixin, CreateView):
    model = Tabela_exame
    form_class = TexameForm
    template_name = 'tabela_exame_form.html'

    def get_success_url(self):
        return reverse('tabela_exame_list')


class TexameUpdate(LoginRequiredMixin, UpdateView):
    model = Tabela_exame
    form_class = TexameForm
    template_name = 'tabela_exame_form.html'

    def get_success_url(self):
        return reverse('tabela_exame_list')


class TexameDelete(LoginRequiredMixin, DeleteView):
    model = Tabela_exame
    template_name = 'tabela_exame_confirm_delete.html'

    def get_success_url(self):
        return reverse('tabela_exame_list')


class TexameListView(LoginRequiredMixin, ListView):
    model = Tabela_exame
    template_name = 'tabela_exame_list.html'

#########


class ConvenioCreate(LoginRequiredMixin, CreateView):
    model = Convenio
    form_class = ConvenioForm
    template_name = 'convenio_form.html'

    def get_success_url(self):
        return reverse('convenio_list')


class ConvenioUpdate(LoginRequiredMixin, UpdateView):
    model = Convenio
    form_class = ConvenioForm
    template_name = 'convenio_form.html'

    def get_success_url(self):
        return reverse('convenio_list')


class ConvenioDelete(LoginRequiredMixin, DeleteView):
    model = Convenio
    template_name = 'convenio_confirm_delete.html'

    def get_success_url(self):
        return reverse('convenio_list')


class ConvenioListView(LoginRequiredMixin, ListView):
    model = Convenio
    template_name = 'convenio_list.html'


#############################
# Views de Atendimento
#############################
class PacienteView(LoginRequiredMixin, CreateView):
    model = Paciente
    template_name = 'paciente_form_inner.html'
    form_class = PacienteForm

    def get_success_url(self):
        return reverse('atendimento_new')


class PacienteUpdateModal(LoginRequiredMixin, UpdateView):
    model = Paciente
    template_name = 'paciente_form_edit_inner.html'
    form_class = PacienteForm

    def get_success_url(self):
        return reverse('atendimento_new')


class AtendimentoCreate(LoginRequiredMixin, CreateView):
    model = Atendimento
    form_class = AtendimentoForm
    template_name = 'atendimento_form.html'

    def get_success_url(self):
        return reverse('atendimento_list')


class AtendimentoUpdate(LoginRequiredMixin, UpdateView):
    model = Atendimento
    form_class = AtendimentoForm
    template_name = 'atendimento_form.html'

    def get_success_url(self):
        return reverse('atendimento_list')


class AtendimentoDelete(LoginRequiredMixin, DeleteView):
    model = Atendimento
    # template_name_suffix = 'templates/'
    template_name = 'atendimento_confirm_delete.html'

    def get_success_url(self):
        return reverse('atendimento_list')


class AtendimentoListView(LoginRequiredMixin, ListView):
    model = Atendimento
    template_name = 'atendimento_list.html'

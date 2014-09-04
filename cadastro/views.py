from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView
from .models import Paciente
from .forms import PacienteForm


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

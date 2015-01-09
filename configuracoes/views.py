from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Posto
from .forms import PostoForm

@login_required(login_url='/login/')
def home(request):
    return render(request, 'index.html')

#############################
# Views do Posto
#############################

class PostoCreate(CreateView):
    model = Posto
    form_class = PostoForm
    template_name = 'posto_form.html'

    def get_success_url(self):
        return reverse('posto_list')

class PostoUpdate(UpdateView):
    model = Posto
    form_class = PostoForm
    template_name = 'posto_form.html'

    def get_success_url(self):
        return reverse('posto_list')


class PostoDelete(DeleteView):
    model = Posto
    # template_name_suffix = 'templates/'
    template_name = 'posto_confirm_delete.html'

    def get_success_url(self):
        return reverse('posto_list')


class PostoListView(ListView):
    model = Posto
    template_name = 'posto_list.html'

###############################################
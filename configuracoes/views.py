from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Posto
from .forms import PostoForm
from login.views import LoginRequiredMixin

#############################
# Views do Posto
#############################


class PostoCreate(LoginRequiredMixin, CreateView):
    model = Posto
    form_class = PostoForm
    template_name = 'posto_form.html'

    def get_success_url(self):
        return reverse('posto_list')


class PostoUpdate(LoginRequiredMixin, UpdateView):
    model = Posto
    form_class = PostoForm
    template_name = 'posto_form.html'

    def get_success_url(self):
        return reverse('posto_list')


class PostoDelete(LoginRequiredMixin, DeleteView):
    model = Posto
    # template_name_suffix = 'templates/'
    template_name = 'posto_confirm_delete.html'

    def get_success_url(self):
        return reverse('posto_list')


class PostoListView(LoginRequiredMixin, ListView):
    model = Posto
    template_name = 'posto_list.html'

###############################################
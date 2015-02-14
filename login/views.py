from django.http import *
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from login.form import UserForm


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    return render_to_response('login.html', context_instance=RequestContext(request))


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


#############################
# Views de Cadastro de Usuário
#############################
class UserCreate(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'user_form.html'

    def get_success_url(self):
        return reverse('user_list')


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user_form.html'

    def get_success_url(self):
        return reverse('user_list')


class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    # template_name_suffix = 'templates/'
    template_name = 'user_confirm_delete.html'

    def get_success_url(self):
        return reverse('user_list')


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user_list.html'

###############################################
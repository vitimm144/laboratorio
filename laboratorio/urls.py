from django.conf.urls import patterns, include, url
from cadastro.views import home, CadastroPacienteView, CadastroMedicoView, CadastroExameView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^paciente/new/$', CadastroPacienteView.as_view(), name='new_paciente'),
    url(r'^medico/new/$', CadastroMedicoView.as_view(), name='new_medico'),
    url(r'^exame/new/$', CadastroExameView.as_view(), name='new_exame'),
    (r'^login/$', 'login.views.login_user'),
    url(r'^admin/', include(admin.site.urls)),
)


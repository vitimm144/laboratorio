from django.conf.urls import patterns, include, url
from cadastro.views import home, CadastroPacienteView, CadastroMedicoView, CadastroExameView, CadastroTexameView, CadastroConvenioView, CadastroAtendimentoView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^paciente/new/$', CadastroPacienteView.as_view(), name='new_paciente'),
    url(r'^medico/new/$', CadastroMedicoView.as_view(), name='new_medico'),
    url(r'^exame/new/$', CadastroExameView.as_view(), name='new_exame'),
    url(r'^tabela_exames/new/$', CadastroTexameView.as_view(), name='new_tabela_exames'),
    url(r'^convenio/new/$', CadastroConvenioView.as_view(), name='new_convenio'),
    url(r'^atendimento/new/$', CadastroAtendimentoView.as_view(), name='new_atendimento'),
    (r'^login/$', 'login.views.login_user'),
    url(r'^admin/', include(admin.site.urls)),
)


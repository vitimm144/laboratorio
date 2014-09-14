from django.conf.urls import patterns, include, url
from cadastro.views import home, CadastroPacienteView, CadastroExameView, CadastroTexameView, CadastroConvenioView, CadastroAtendimentoView
from django.contrib import admin
from cadastro.views import MedicoCreate, MedicoDelete, MedicoUpdate, MedicoListView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^paciente/new/$', CadastroPacienteView.as_view(), name='new_paciente'),
    url(r'^medico/new/$', MedicoCreate.as_view(), name='medico_new'),
    url(r'^medicos/$', MedicoListView.as_view(), name='medico_list'),
    url(r'^medico/(?P<pk>[0-9]+)/$', MedicoUpdate.as_view(), name='medico_edit'),
    url(r'^medico/(?P<pk>[0-9]+)/delete/$', MedicoDelete.as_view(), name='medico_delete'),
    url(r'^exame/new/$', CadastroExameView.as_view(), name='new_exame'),
    url(r'^tabela_exames/new/$', CadastroTexameView.as_view(), name='new_tabela_exames'),
    url(r'^convenio/new/$', CadastroConvenioView.as_view(), name='new_convenio'),
    url(r'^atendimento/new/$', CadastroAtendimentoView.as_view(), name='new_atendimento'),
    (r'^login/$', 'login.views.login_user'),
    url(r'^admin/', include(admin.site.urls)),
)


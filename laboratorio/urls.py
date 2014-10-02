from django.conf.urls import patterns, include, url
from cadastro.views import home
from django.contrib import admin
from cadastro.views import MedicoCreate, MedicoDelete, MedicoUpdate, MedicoListView
from cadastro.views import PacienteListView, PacienteCreate, PacienteDelete, PacienteUpdate
from cadastro.views import ExameCreate, ExameDelete, ExameUpdate, ExameListView
from cadastro.views import AtendimentoCreate, AtendimentoDelete, AtendimentoUpdate, AtendimentoListView
from cadastro.views import ConvenioCreate, ConvenioDelete, ConvenioListView, ConvenioUpdate
from cadastro.views import TexameCreate, TexameDelete, TexameUpdate, TexameListView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^paciente/new/$', PacienteCreate.as_view(), name='paciente_new'),
    url(r'^pacientes/$', PacienteListView.as_view(), name='paciente_list'),
    url(r'^paciente/(?P<pk>[0-9]+)/$', PacienteUpdate.as_view(), name='paciente_edit'),
    url(r'^paciente/(?P<pk>[0-9]+)/delete/$', PacienteDelete.as_view(), name='paciente_delete'),
    url(r'^medico/new/$', MedicoCreate.as_view(), name='medico_new'),
    url(r'^medicos/$', MedicoListView.as_view(), name='medico_list'),
    url(r'^medico/(?P<pk>[0-9]+)/$', MedicoUpdate.as_view(), name='medico_edit'),
    url(r'^medico/(?P<pk>[0-9]+)/delete/$', MedicoDelete.as_view(), name='medico_delete'),
    url(r'^exame/new/$', ExameCreate.as_view(), name='exame_new'),
    url(r'^exames/$', ExameListView.as_view(), name='exame_list'),
    url(r'^exame/(?P<pk>[0-9]+)/$', ExameUpdate.as_view(), name='exame_edit'),
    url(r'^exame/(?P<pk>[0-9]+)/delete/$', ExameDelete.as_view(), name='exame_delete'),
    url(r'^tabela_exame/new/$', TexameCreate.as_view(), name='tabela_exame_new'),
    url(r'^tabela_exames/$', TexameListView.as_view(), name='tabela_exame_list'),
    url(r'^tabela_exame/(?P<pk>[0-9]+)/$', TexameUpdate.as_view(), name='tabela_exame_edit'),
    url(r'^tabela_exame/(?P<pk>[0-9]+)/delete/$', TexameDelete.as_view(), name='tabela_exame_delete'),
    url(r'^convenio/new/$', ConvenioCreate.as_view(), name='convenio_new'),
    url(r'^convenios/$', ConvenioListView.as_view(), name='convenio_list'),
    url(r'^convenio/(?P<pk>[0-9]+)/$', ConvenioUpdate.as_view(), name='convenio_edit'),
    url(r'^convenio/(?P<pk>[0-9]+)/delete/$', ConvenioDelete.as_view(), name='convenio_delete'),
    url(r'^atendimento/new/$', AtendimentoCreate.as_view(), name='atendimento_new'),
    url(r'^atendimentos/$', AtendimentoListView.as_view(), name='atendimento_list'),
    url(r'^atendimento/(?P<pk>[0-9]+)/$', AtendimentoUpdate.as_view(), name='atendimento_edit'),
    url(r'^atendimento/(?P<pk>[0-9]+)/delete/$', AtendimentoDelete.as_view(), name='atendimento_delete'),
    (r'^login/$', 'login.views.login_user'),
    url(r'^admin/', include(admin.site.urls)),
)


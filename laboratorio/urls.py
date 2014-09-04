from django.conf.urls import patterns, include, url
from cadastro.views import home, CadastroPacienteView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^paciente/new/$', CadastroPacienteView.as_view(), name='new_paciente'),
    (r'^login/$', 'login.views.login_user'),
    url(r'^admin/', include(admin.site.urls)),
)


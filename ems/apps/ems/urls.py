from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = (
    path('', views.index, name='homepage'),
    path('interfaces', views.interfaces, name='ems_interfaces'),
    path('interface/<slug:interface>',
         views.element, name='ems_interface'),
    #     path('edit/interface/<slug:interface>',
    #          views.element, name='edit-interface'),
    path('logs', views.ems_logs, name='ems_logs'),
    path('alarms', views.ems_alarms, name='ems_alarms'),
    path('events', views.ems_events, name='ems_events'),
    path('cdr', views.ems_cdr, name='ems_cdr'),
    path('help', views.help, name='ems_help'),
    path('temperature', views.ems_temperature, name='ems_temperature'),

    path('update_software', views.ems_update_software, name='ems_update_software'),

    path('import', views.ems_import, name='ems_import'),
    path('export', views.ems_export, name='ems_export'),

    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('create',views.create,name='create'),
)

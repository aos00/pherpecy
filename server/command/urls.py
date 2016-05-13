from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^command_output/$', views.upload_file, name='command_output'),
]
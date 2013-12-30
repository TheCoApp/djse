from django.conf.urls import patterns, url
from thr import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))


__author__ = 'johnanderson1'
from django.conf.urls import patterns,url
from sampledata import views


urlpatterns = patterns('',url(r'^$',views.index,name='index'), )
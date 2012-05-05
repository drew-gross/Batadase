from django.conf.urls.defaults import patterns, include, url

from api import views

urlpatterns = patterns('api',
                       url(r'(?P<key>.*)$', views.key,),
                       )
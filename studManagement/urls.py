from django.conf.urls import patterns, include, url
from studManagement.views import hello

urlpatterns = patterns('',
    url(r'^hello/$', hello),
)

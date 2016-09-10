# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from views import RegistrantListCreateView
from views import RegistrantUpdateView


urlpatterns = patterns(
    '',
    url(r'^/registrants$', RegistrantListCreateView.as_view()),
    url(r'^/registrants/(?P<pk>\d+)$', RegistrantUpdateView.as_view()),
)

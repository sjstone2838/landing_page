# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from views import RegistrantCreateUpdateView


urlpatterns = patterns(
    '',
    url(r'^/registrants$', RegistrantCreateUpdateView.as_view()),
)

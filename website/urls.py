# -*- coding: utf-8 -*-
from django.conf.urls import patterns
# from . import views


urlpatterns = patterns('website.views',
                       (r'^$', 'index'),
                       )

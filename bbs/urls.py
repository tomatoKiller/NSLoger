# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from bbs import views


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^recent/?$',views.recent, name='recent'),
        url(r'^t/(?P<topic_id>\d+)/$', views.topic, name="topic"),
        url(r'^topic/(\d+)/reply/?$',views.reply,name='reply'),
        url(r'^topic/([\w-]+)/new/?$',views.new,name='new'),
        url(r'^node/(?P<node_slug>[\w-]+)/$',views.node,name="node"),
        )

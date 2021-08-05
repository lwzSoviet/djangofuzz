#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""
    @Description: 
    ~~~~~~
    @Author  : pake
    @Time    : 2021/7/13 15:20
"""
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),



    path('send/', views.send, name='send'),
]
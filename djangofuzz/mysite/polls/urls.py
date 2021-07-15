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

urlpatterns = [
    path('', views.index, name='index'),
]
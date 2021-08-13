#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @Description: 
    ~~~~~~
    @Author  : pake
    @Time    : 2021/8/10 16:18
"""
import os

from django import forms
from django.core.files.images import get_image_dimensions
from django.core.files.storage import Storage

if __name__=='__main__':
    # file = forms.FilePathField(path='D:\\aaa\\aaaa',recursive=True)
    # class SubStorage(Storage):
    #     def exists(self, name):
    #         if os.path.exists(name):
    #             return True
    # a=SubStorage()
    # a.get_available_name('D:\\aaaaaaaaaaaaaaaaaaa.t',12)
    print(get_image_dimensions('C:\\Users\jliu\PycharmProjects\djangofuzz\djangofuzz\mysite\polls\static\\1.jpg'))

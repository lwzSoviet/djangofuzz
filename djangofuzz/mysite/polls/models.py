import os
from django.conf import settings
from django.db import models

# Create your models here.
from django import forms

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)



class FilePathFieldForm(forms.Form):
    file = forms.FilePathField(path='C:\\Users\jliu\PycharmProjects\\djangofuzz\\djangofuzz\mysite\polls\static\\')





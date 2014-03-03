#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django import forms
from bbs.models import Topic, Comment

class TopicForm(forms.ModelForm):
    title = forms.CharField(label=u'标题',min_length=1,widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(label=u'内容',max_length=1000,min_length=1,widget=forms.Textarea(attrs={'class':'form-control','rows':'10'}))   
    class Meta:
        model = Topic
        fields = ('title','content')

  
class ReplyForm(forms.ModelForm):
    content = forms.CharField(max_length=1000,min_length=1,widget=forms.Textarea(attrs={'class':'form-control','rows':'5'})) 
    class Meta:
        model = Comment
        fields = ('content',)

class EditForm(forms.Form):
    content = forms.CharField(label=u'内容',max_length=1000,widget=forms.Textarea(attrs={'class':'form-control','rows':'20'}))   
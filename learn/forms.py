# -*- coding: utf-8 -*-
from django import forms


class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()


class AddTestForm(forms.Form):
    name = forms.CharField()
    tag_line = forms.CharField()
from django import forms
from .models import baikemodel


class baikeform(forms.ModelForm):
    class Meta:
        model = baikemodel
        fields = ['title' 'ent']

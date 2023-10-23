from django import forms
from .models import *

class TalabaForm(forms.Form):
    i=forms.CharField(label="Ism")
    k=forms.IntegerField(label="Kurs", max_value=7,min_value=1)
    k_s=forms.IntegerField(label="Kitoblari soni")

class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields="__all__"

class KitobForm(forms.ModelForm):
    class Meta:
        model=Kitob
        fields = "__all__"
from django import forms
from django.forms import fields
from app.blog.models import IletisimModel

class IletisimForm(forms.ModelForm):
    class Meta:
        model = IletisimModel
        fields = ('isim_soyisim','email','mesaj')
    

'''
class IletisimForm(forms.Form):
    email = forms.EmailField(max_length=100, label='ePosta')
    isim_soyisim = forms.CharField(max_length=100, label='Ad Soyad')
    mesaj = forms.CharField(label='Mesajınız',widget=forms.Textarea())


class IletisimForm(forms.Form):
    email = forms.EmailField(max_length=100, label='ePosta',widget=forms.TextInput(attrs={'class':'form-control'}))
    isim_soyisim = forms.CharField(max_length=100, label='Ad Soyad',widget=forms.TextInput(attrs={'class':'form-control'}))
    mesaj = forms.CharField(label='Mesajınız',widget=forms.Textarea(attrs={
        'class':'form-control'
    }))
'''
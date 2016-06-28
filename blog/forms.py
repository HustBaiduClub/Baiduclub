__author__ = 'david'
from django import forms
from captcha.fields import CaptchaField


class CaptchaTestForm(forms.Form):
    blog = forms.CharField(max_length=200)
    user = forms.CharField(max_length=254)
    email = forms.EmailField(max_length=100)
    content = forms.CharField(widget=forms.Textarea, max_length=500)
    captcha = CaptchaField()

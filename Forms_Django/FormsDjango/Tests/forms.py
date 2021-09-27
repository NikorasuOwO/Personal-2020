from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label="Your e-mail", max_length=100)
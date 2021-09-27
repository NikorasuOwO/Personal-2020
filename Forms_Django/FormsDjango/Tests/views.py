from django import forms
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import NameForm

# Create your views here.

def thanks(request, info=""):

    return HttpResponse("Thank you very much " + info['name'] +". We successfully registered your e-mail: "+ info['email'])

def form1(request):
    data = {}
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            #return thanks(request, info=form.cleaned_data)
            data['name'] = form.cleaned_data['name']

    form = NameForm(data)

    return render(request, 'Tests/form1.html', {"form":form})
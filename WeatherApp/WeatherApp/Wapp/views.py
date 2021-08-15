from django.shortcuts import render
from . import weather_api

# Create your views here.

def show(request):

    json = weather_api.test()

    context = {}
    context['raw'] = json
    context['icon'] = json['weather'][0]['icon']
    context['temp'] = round( json['main']['temp'] )

    return render(request, 'Wapp/index.html', context)
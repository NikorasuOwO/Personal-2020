from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from . import weather_api, codes
import requests
from .models import *
from datetime import datetime, timedelta
from googletrans import Translator

# Create your views here.

def update_database(request):
    from Wapp.models import Code
    Code.objects.all().delete()
    Code.update_database()
    return redirect('home')

def notfound(request):
    return render(request, 'Wapp/404error.html', {})

def show(request, lang=None):

# Fetching the data
    context={}
    if request.method == 'POST':
        if request.POST['lang'] is not None:
            lang = "lang=" + request.POST.get('lang')
            #if lang == 'lang=ar': return HttpResponse("city: " + str(request.POST['city']) + "| lang:" + str(request.POST['lang']) +"\n")
        json = weather_api.test(request.POST['city'], request.POST['country'], lang)
        if json['cod'] != "200":
            json = requests.get("https://api.openweathermap.org/data/2.5/forecast?units=metric&zip=94040,us&appid=78b961904399670d2db35232076db668").json()
            #return HttpResponse("city: " + str(request.POST['city']) + "| country:" + str(request.POST['country']) +"\n"+ str(json['get']))
    else:
        json = requests.get("https://api.openweathermap.org/data/2.5/forecast?units=metric&zip=94040,us&appid=78b961904399670d2db35232076db668").json()

# Processing the data

    class info_day:

        def __init__(self, icon, temp, min, max, description, day):

            self.icon = icon
            self.temp = temp
            self.min = min
            self.max = max
            self.description = description
            self.day = day

    translator = Translator() # Making a translator object to translate words
    lang_target = lang.split('=')[1] #Extracting 'a' from 'lang=a'. e.g. we extract 'es' from 'lang=es'

    today = datetime.today()
    day3 = (today + timedelta(2)).strftime("%d/%m") # Today +1 = tomorrow, today + 1 = day3
    day4 = (today + timedelta(3)).strftime("%d/%m") # same idea
    today = translator.translate('Today', dest=lang_target).text # "today" is translated to the target language
    tomorrow = translator.translate('Tomorrow', dest=lang_target).text # idem with Tomorrow

    dayname_list = [today, tomorrow, day3, day4]

    reduced_list= []

    for item in json['list'][:4]:
        obj = info_day(
            item['weather'][0]['icon'],
            round(item['main']['temp']),
            round(item['main']['temp_min']),
            round(item['main']['temp_max']),
            item['weather'][0]['description'],
            dayname_list.pop(0)
        )
        reduced_list.append(obj)

    context['reduced_list'] = reduced_list
    context['country_codes'] = Code.objects.all()
    context['raw'] = json
    context['current_city'] = json['city']['name']
    context['current_country'] = Code.objects.get(code=json['city']['country']).name
    #context['current_lang'] = json['lang']
    context['lang'] = lang_target
    return render(request, 'Wapp/index.html', context)
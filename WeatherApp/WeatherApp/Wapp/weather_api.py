
import requests


def add_conditions(*args, base):

    final = base + args[0]

    for arg in args[1:]:
        final = final + '&' + arg

    return final


def test(city, country_code, lang):
    
    apikey = 'appid=78b961904399670d2db35232076db668'
    city='q=' + city + "," + country_code
    units= "units=metric"
    #url = 'https://api.openweathermap.org/data/2.5/weather?'
    url = 'https://api.openweathermap.org/data/2.5/forecast?'
    #exclude = 'exclude=hourly,minutely,current,alerts'
    url_to_get = add_conditions(city, apikey, units, lang, base=url)
    json_final = requests.get(url_to_get).json()
    json_final['get'] = url_to_get
    
    return json_final
    
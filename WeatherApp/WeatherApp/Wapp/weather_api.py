
import requests


def add_conditions(*args, base):

    final = base + args[0]

    for arg in args[1:]:
        final = final + '&' + arg

    return final


def test():

    apikey = 'appid=78b961904399670d2db35232076db668'
    city='q=Valencia'
    units= "units=metric"
    url = 'https://api.openweathermap.org/data/2.5/weather?'

    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Valencia&appid=78b961904399670d2db35232076db668&units=metric")

    test = add_conditions(city, apikey, units, base=url)

    return requests.get(test).json()

#print(test)
#print(requests.get(test).json())
#print(requests.get(test).json())
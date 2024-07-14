from django.shortcuts import render,HttpResponse
import requests
import datetime
import math
import creds

# Create your views here.

def index(request):
    if request.method == "POST":
        city = request.POST["location"]
        timezone = datetime.datetime.fromtimestamp(get_weather(city)['timezone'])
        sunrise = datetime.datetime.fromtimestamp(get_weather(city)['sys']['sunrise'])
        sunrset = datetime.datetime.fromtimestamp(get_weather(city)['sys']['sunset'])
        temp = math.floor(get_weather(city)['main']['temp']) - 273
        feelslike = math.floor(get_weather(city)['main']['feels_like']) - 273
        tempmax = math.floor(get_weather(city)['main']['temp_max']) - 273
        tempmin = math.floor(get_weather(city)['main']['temp_min']) - 273
    
        context = {'weather_data': get_weather(city),
                   'weather': get_weather(city)['weather'][0]['main'],
                   'humidity': get_weather(city)['main']['humidity'],
                   'visibility': get_weather(city)['visibility'],
                   'pressure': get_weather(city)['main']['pressure'],
                   'windspeed': get_weather(city)['wind']['speed'],
                   'winddeg': get_weather(city)['wind']['deg'],
                   'cityname': get_weather(city)['name'],
                   'country': get_weather(city)['sys']['country'],
                   'latitude': get_weather(city)['coord']['lat'],
                   'longitude': get_weather(city)['coord']['lon'],
                   'timezone': timezone,
                   'sunrise': sunrise,
                   'sunset': sunrset,
                   'tempmax': tempmax,
                   'tempmin': tempmin,
                   'temp': temp,
                   'feelslike': feelslike,
                   'icon': get_weather(city)['weather'][0]['icon']
                }
        return render(request, 'index.html', context)
    else:
        context = {'weather_data': '--',
                   'weather': '--',
                   'humidity': '--',
                   'visibility': '--',
                   'pressure': '--',
                   'windspeed': '--',
                   'winddeg': '--',
                   'cityname': '--',
                   'country': '--',
                   'latitude': '--',
                   'longitude': '--',
                   'timezone': '--',
                   'sunrise': '--',
                   'sunset': '--',
                   'tempmax': '--',
                   'tempmin': '--',
                   'temp': '--',
                   'feelslike': '--',
                   'icon': '02d'
                }
        return render(request, 'index.html', context)
        
    

def get_weather(city):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={creds.API_KEY}"
    response = requests.get(api_url)
    data = response.json()
    return data
from django.shortcuts import render
import requests
import datetime
import math
import creds

def index(request):
    if request.method == "POST":
        city = request.POST.get("location")
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={creds.API_KEY}"
        response = requests.get(api_url)
        weather_data = response.json()
        city = request.POST["location"]
        tz_offset_seconds = int(weather_data['timezone'])
        utc_timestamp = datetime.datetime.utcnow().timestamp()
        local_timestamp = utc_timestamp + tz_offset_seconds
        timezone = datetime.datetime.fromtimestamp(local_timestamp)
        sunrise = datetime.datetime.fromtimestamp(weather_data['sys']['sunrise'])
        sunrset = datetime.datetime.fromtimestamp(weather_data['sys']['sunset'])
        temp = math.floor(weather_data['main']['temp']) - 273
        feelslike = math.floor(weather_data['main']['feels_like']) - 273
        tempmax = math.floor(weather_data['main']['temp_max']) - 273
        tempmin = math.floor(weather_data['main']['temp_min']) - 273
        
        context = {'weather_data': weather_data,
                   'weather': weather_data['weather'][0]['main'],
                   'humidity': weather_data['main']['humidity'],
                   'visibility': weather_data['visibility'],
                   'pressure': weather_data['main']['pressure'],
                   'windspeed': weather_data['wind']['speed'],
                   'winddeg': weather_data['wind']['deg'],
                   'cityname': weather_data['name'],
                   'country': weather_data['sys']['country'],
                   'latitude': weather_data['coord']['lat'],
                   'longitude': weather_data['coord']['lon'],
                   'timezone': timezone,
                   'sunrise': sunrise,
                   'sunset': sunrset,
                   'tempmax': tempmax,
                   'tempmin': tempmin,
                   'temp': temp,
                   'feelslike': feelslike,
                   'icon': weather_data['weather'][0]['icon']
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
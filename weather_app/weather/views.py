import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=516bd0bd00a16ad85bf29cdd8e8fc2d7"
    
    
    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    
    cities = City.objects.all()
    weather_data = []
    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature': r['main']['temp'],
            'humidity': r['main']['humidity'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    weather_data = weather_data[-1:]
    args = {
        'weather_data' : weather_data,
        'form': form,
    }
    
    return render(request, 'weather/weather.html', args)
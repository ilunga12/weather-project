from multiprocessing import context

from django.contrib.sites import requests
from django.shortcuts import render, redirect
import requests

from appweather.forms import CityForm
from appweather.models import City


# Create your views here.
def Weather(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q=las%20vegas&units=imperial&appid=05538d035642047e40465c53ad0aad31"
    city = 'england'
    cities = City.objects.all()
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        print(city_weather)
        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']

        }
        weather_data.append(weather)

    context = {'weather_data': weather_data,'form' : form}
    return render(request, "weather.html",context )


def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()

    return redirect('Weather')



from django.urls import path

from appweather import views

urlpatterns = [
    path("",views.Weather,name="Weather"),
    path('delete/<city_name>/', views.delete_city, name='delete_city')

]
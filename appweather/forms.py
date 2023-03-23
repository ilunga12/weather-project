from django.forms import ModelForm, TextInput

from appweather.models import City


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name':TextInput(attrs={'class' : 'input','placholder' : 'City Name'})
        }
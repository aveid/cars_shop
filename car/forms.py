from django import forms

from car.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        # fields = ("vin", "color", "price", "description", "year", "model")
        exclude = ("owner",)


from django.shortcuts import render
from django.views import generic

from car.models import Car


class CarListView(generic.ListView):
    model = Car
    template_name = "car.html"
    context_object_name = "cars"

# def get_detail(request, pk):
#     car = Car.objects.get(id=pk)
#     return render(request, "car-single.html", locals())

class CarDetailView(generic.DetailView):
    model = Car
    template_name = "car-single.html"
    context_object_name = "car"


class PriceListView(generic.ListView):
    model = Car
    template_name = "pricing.html"


from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic

from car.forms import CarForm
from car.models import Car



# def get_cars(request):
#     search = request.GET.get("search")
#     cars = Car.objects.all()
#     if search:
#         cars = Car.objects.filter(Q(model__name__icontains=search) |
#                                   Q(model__brand__name__icontains=search)
#                                   )
#
#     brands = Brand.objects.all()
#     return render(request, "car.html", locals())


class CarListView(generic.ListView):
    model = Car
    template_name = "car.html"
    context_object_name = "cars"

    def get_queryset(self):
        search = self.request.GET.get("search")
        cars = Car.objects.all()
        if search:
            cars = Car.objects.filter(Q(model__name__icontains=search) |
                                      Q(model__brand__name__icontains=search)
                                      )
        return cars


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


class CarCreateView(generic.CreateView):
    model = Car
    form_class = CarForm
    template_name = "create_car.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("cars")
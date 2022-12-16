from django.urls import path
from . import views

urlpatterns = [
    path("", views.CarListView.as_view(), name="cars"),
    path("detail/<int:pk>/", views.CarDetailView.as_view(), name="car_detail"),
    path("pricing/", views.PriceListView.as_view(), name="car_price"),
 ]

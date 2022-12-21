from django.db import models
from django.contrib.auth import get_user_model
from categories.models import ModelCar

User = get_user_model()


class Car(models.Model):
    vin = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=100, decimal_places=10)
    color = models.CharField(max_length=16)
    description = models.TextField()
    year = models.PositiveSmallIntegerField()
    model = models.ForeignKey(ModelCar,
                              on_delete=models.SET_NULL,
                              null=True,
                              related_name="cars"
                              )
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.model.name} - {self.price}"


class Image(models.Model):
    image = models.ImageField(upload_to="car")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="images")

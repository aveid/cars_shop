from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ModelCar(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.ForeignKey(Brand, verbose_name="Марка машины",
                              on_delete=models.SET_NULL, related_name="models",
                              null=True)

    def __str__(self):
        return self.name

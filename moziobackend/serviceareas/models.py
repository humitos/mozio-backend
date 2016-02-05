from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Provider(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = PhoneNumberField()
    language = models.CharField(max_length=2)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    polygon = models.PolygonField()
    provider = models.ForeignKey('Provider')

    def __str__(self):
        return self.name

# providers.objects.filter(servicearea_set__polygon__within=point)
# servicearea.objects.filter(polygon__within=point)

from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Provider(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = PhoneNumberField()
    # https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    language = models.CharField(max_length=2)  # iso639-1
    # http://www.xe.com/iso4217.php
    currency = models.CharField(max_length=3)  # iso4217

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    polygon = models.PolygonField()
    provider = models.ForeignKey('Provider')

    def __str__(self):
        return self.name

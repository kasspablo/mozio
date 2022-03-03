from django.db import models

# Create your models here.

LANGUAGE_CHOICES = [
    ('ENG', 'English'),
    ('SPA', 'Spanish'),
]

CURRENCY_CHOICES = [
    ('USD', 'US Dollar'),
    ('EUR', 'Euro'),
]

class Provider(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length = 20)
    language = models.CharField(max_length = 3, choices = LANGUAGE_CHOICES)
    currency = models.CharField(max_length = 3, choices = CURRENCY_CHOICES)

    def __str__(self):
        return self.name


class PolygonZone(models.Model):
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits =7 , decimal_places = 2, default = 0.00 )
    polygon = models.TextField()

    def __str__(self):
        return self.name
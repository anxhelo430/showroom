from django.db import models

# Create your models here.

class cars(models.Model):
    cars_slug = models.SlugField(primary_key=True)
    cars_name = models.CharField(max_length=200, null=True, blank=True)
    cars_description = models.TextField(null=True, blank=True)
    cars_price = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)
    cars_image = models.ImageField(upload_to= 'cars/')
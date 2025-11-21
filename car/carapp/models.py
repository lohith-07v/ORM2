from django.db import models
from django.contrib import admin
class Car (models.Model):
    brand_name=models.CharField(max_length=100)
    car_name=models.CharField(max_length=100)
    enginenum=models.IntegerField()
    release_date=models.DateField()

class carAdmin(admin.ModelAdmin):
    list_display=('brand_name','car_name','enginenum','release_date')
# Create your models here.

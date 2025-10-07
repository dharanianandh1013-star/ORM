from django.db import models
from django.contrib import admin

class car(models.Model):
    name = models.CharField(max_length=255, help_text="Car Name")
    model = models.CharField(max_length=50, unique=True, help_text="model")
    color = models.CharField(max_length=100, help_text="Color (e.g., black , white , blue , green)")
    manufacturing_date = models.DateField()    
    Horse_power = models.IntegerField()
class modelAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'color',"manufacturing_date","Horse_power")

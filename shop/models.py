from django.db import models

# Create your models here.
class Item(models.Model):
    category = models.CharField(max_length=90)
    item_name = models.CharField(max_length=90)
    item_type = models.CharField(max_length=90)
    quantity =models.IntegerField(default=0)
    price  =   models.FloatField()
    item_image = models.CharField(max_length=200)
    rating =models.IntegerField(default=5)



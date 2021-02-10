from django.db import models
from menu.models import Meal
# Create your models here.


class MealOrder(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_phone_number = models.CharField(max_length=20)
    customer_adress = models.CharField(max_length=70)
    customer_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    customer_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    order_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    order_modified = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.customer_name


class OrderUnit(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='units')
    quantity = models.IntegerField()
    order = models.ForeignKey(MealOrder, on_delete=models.CASCADE, related_name='order_units')

    def __str__(self):
        return self.meal+str(self.quantity)

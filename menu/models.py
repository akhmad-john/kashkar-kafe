from django.db import models

# Create your models here.


class MealSection(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Meal(models.Model):
    section = models.ForeignKey(MealSection, on_delete=models.SET_NULL, null=True)
    name =  models.CharField(max_length=25)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    is_active = models.BooleanField(default=True)
    description = models.TextField()
    image = models.ImageField(upload_to='meal_photos/', null=True, default=None, blank=False)

    def __str__(self):
        return self.name
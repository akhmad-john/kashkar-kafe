from django.contrib import admin
from .models import MealSection, Meal
# Register your models here.

class MealAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_section_name', 'price', 'image')
    list_filter = ('section__name',)

    def get_section_name(self, obj):
        return obj.section.name

admin.site.register(MealSection)
admin.site.register(Meal, MealAdmin)
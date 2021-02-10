from rest_framework import serializers
from .models import *


class MealSectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealSection
        fields = ['id', 'name']
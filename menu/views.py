from django.shortcuts import render
from rest_framework import generics
from .models import * 
from .serializers import *

# Create your views here.
class MealSectionListView(generics.ListAPIView):
    queryset = MealSection.objects.all()
    serializer_class = MealSectionListSerializer
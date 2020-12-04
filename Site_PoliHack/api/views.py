from django.shortcuts import render
from rest_framework import generics
from .serializers import ClasaSerializer
from .models import Clasa
from django.db import models
# Create your views here.

class ClassView( generics.CreateAPIView ) :

    queryset = Clasa.objects.all()
    serializer_class = ClasaSerializer

from django.shortcuts import render
from rest_framework import generics
from .models import Teknik
from .serializers import TeknikSerializers


class TeknikListCreate(generics.ListCreateAPIView):
    queriset = Tutorial.objects.all()
    serializers_class =TutorialSerializers
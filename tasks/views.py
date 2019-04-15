from django.shortcuts import render
from rest_framework import viewsets
from .models import Tasks
from .serializers import LanguageSerializer

class TaskView(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class =  LanguageSerializer


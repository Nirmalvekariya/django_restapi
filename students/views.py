from django.shortcuts import render
from rest_framework import viewsets
from .models import Students
from .serializers import StudentsSerializer


class StudentsView(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class =  StudentsSerializer

def home(request):
    return render(request,"home.html",{})
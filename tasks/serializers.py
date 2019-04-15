from rest_framework import serializers
from .models import Tasks

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'Task_Name', 'Task_Description')
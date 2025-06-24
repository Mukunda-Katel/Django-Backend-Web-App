from rest_framework import serializers
from .models import LessonResources

class LessonResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonResources
        fields = ['id', 'lesson', 'resource_file', 'description', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']

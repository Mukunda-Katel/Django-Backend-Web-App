from rest_framework import serializers
from .models import Notices

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notices
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']





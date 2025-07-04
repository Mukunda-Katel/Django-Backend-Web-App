from rest_framework import serializers
from .models import Notices, Notification, UpcomingCourse, UpcomingCourseNotification

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notices
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class UpcomingCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcomingCourse
        fields = '__all__'

class UpcomingCourseNotificationSerializer(serializers.ModelSerializer):
    upcoming_course_id = serializers.IntegerField(source='upcoming_course.id', read_only=True)
    upcoming_course_title = serializers.CharField(source='upcoming_course.title', read_only=True)
    class Meta:
        model = UpcomingCourseNotification
        fields = '__all__'
        extra_fields = ['upcoming_course_id', 'upcoming_course_title']





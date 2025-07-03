from rest_framework import serializers
from courses.models import Courses, Weeks, Lessons, Videos

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ['videos_url']

class LessonSerializer(serializers.ModelSerializer):
    video = VideoSerializer(read_only=True)
    
    class Meta:
        model = Lessons
        fields = ['title', 'description', 'video', 'order']

class WeekSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    
    class Meta:
        model = Weeks
        fields = ['number', 'title', 'lessons']

class CourseDetailSerializer(serializers.ModelSerializer):
    weeks = WeekSerializer(many=True, read_only=True)
    
    class Meta:
        model = Courses
        fields = ['id', 'title', 'description', 'creator', 'price', 'duration', 'weeks']

class WeekOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Weeks
        fields = ['id', 'number', 'title']

class LessonOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ['id', 'title', 'description', 'order'] 
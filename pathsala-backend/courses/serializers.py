from rest_framework import serializers
from .models import Courses, Weeks, Lessons, Videos



class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ['id', 'title', 'description', 'video_url', 'order']

class WeekSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Weeks
        fields = ['id', 'number', 'title', 'lessons']

class CourseSerializer(serializers.ModelSerializer):
    weeks = WeekSerializer(many=True, read_only=True)

    class Meta:
        model = Courses
        fields = [
            'id', 'title', 'description', 'creator',
            'price', 'created_at', 'category', 'duration', 'weeks'
        ]


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ['id','title','description','video_url','order']
    
class WeekSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True,read_only=True)
    class Meta:
        model = Weeks
        fields = ['id','number','title','lessons']

class LessonWithVideoIDsSerializer(serializers.ModelSerializer):
    video_id = serializers.PrimaryKeyRelatedField(read_only=True, source='video')
    class Meta:
        model = Lessons
        fields = ['id', 'title', 'description', 'video_id']

class VideoURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ['id', 'videos_url']
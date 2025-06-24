from rest_framework import serializers
from .models import Courses



from .models import Courses, Weeks, Lessons

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
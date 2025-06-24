# from rest_framework import serializers
# from .models import Courses,Enrollments,Notices,Certificates

# class CourseSerializer(serializers.ModelSerializer):
#     category_title = serializers.CharField(source='category.category_title', read_only=True)

#     class Meta:
#         model = Courses
#         fields = ['id', 'title', 'description', 'creator', 'price', 'category_title']

# class EnrolledCourseSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(source='course.title')
#     # thumbnail = serializers.ImageField(source='course.thumbnail')  # Make sure 'thumbnail' exists in Courses
#     link = serializers.SerializerMethodField()
#     progress = serializers.DecimalField(max_digits=5, decimal_places=2)

#     class Meta:
#         model = Enrollments
#         fields = ['name', 'link', 'progress']

#     def get_link(self, obj):
#         return f"/student/course/{obj.course.id}"

# class NoticeSerializer(serializers.ModelSerializer):
#     enrolled_course = serializers.CharField(source='course.title',read_only=True)
#     class Meta:
#         model = Notices
#         fields = ['notice_title','notice_description','notice_issued','enrolled_course']


# class CertificateSerializer(serializers.ModelSerializer):
#     enrollment = serializers.CharField(source='enrollment.enrolled_student.name')
#     class Meta:
#         model = Certificates
#         fields = '__all__'
        
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name']

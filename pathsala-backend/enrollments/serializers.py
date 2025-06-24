from rest_framework import serializers
from .models import Enrollments,Certificates
class EnrolledCourseSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='course.title')
    # thumbnail = serializers.ImageField(source='course.thumbnail')  # Make sure 'thumbnail' exists in Courses
    link = serializers.SerializerMethodField()
    progress = serializers.DecimalField(max_digits=5, decimal_places=2)
    course_id = serializers.IntegerField(source='course.id',read_only=True)

    class Meta:
        model = Enrollments
        fields = ['name', 'link', 'progress','course_id']

    def get_link(self, obj):
        return f"/student/course/{obj.course.id}"

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificates
        fields = ['id', 'enrollment', 'certificate_file', 'issued_date']
        read_only_fields = ['id', 'issued_date']

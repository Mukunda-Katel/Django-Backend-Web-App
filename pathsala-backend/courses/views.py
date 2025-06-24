from rest_framework import generics, permissions

from .models import Courses
from .serializers import CourseSerializer

class CourseListAPIView(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]

# class CourseDetailAPIView(generics.RetrieveAPIView):
#     queryset = Courses.objects.all()
#     serializer_class = CourseSerializer
#     permission_classes = [permissions.IsAuthenticated]

class AdminCourseAPIView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView, generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]

class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Courses.objects.prefetch_related('weeks__lessons')
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

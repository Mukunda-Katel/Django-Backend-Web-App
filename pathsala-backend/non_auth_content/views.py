from django.shortcuts import render
from rest_framework import generics
from courses.models import Courses
from .serializers import CourseDetailSerializer

# Create your views here.

class PublicCourseListView(generics.ListAPIView):
    """
    API view to list all courses with their weeks and lessons for non-authenticated users
    """
    queryset = Courses.objects.all().prefetch_related('weeks', 'weeks__lessons', 'weeks__lessons__video')
    serializer_class = CourseDetailSerializer

class PublicCourseDetailView(generics.RetrieveAPIView):
    """
    API view to get a specific course details with its weeks and lessons for non-authenticated users
    """
    queryset = Courses.objects.all().prefetch_related('weeks', 'weeks__lessons', 'weeks__lessons__video')
    serializer_class = CourseDetailSerializer



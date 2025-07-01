from django.shortcuts import render
from rest_framework import generics
from courses.models import Courses, Weeks, Lessons
from .serializers import CourseDetailSerializer, WeekOnlySerializer, LessonOnlySerializer

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

class PublicCourseWeeksListView(generics.ListAPIView):
    """
    API view to list all weeks for a course (no authentication required)
    """
    serializer_class = WeekOnlySerializer
    permission_classes = []

    def get_queryset(self):
        course_id = self.kwargs["course_id"]
        return Weeks.objects.filter(course_id=course_id)

class PublicWeekLessonsListView(generics.ListAPIView):
    """
    API view to list all lessons for a week (no authentication required)
    """
    serializer_class = LessonOnlySerializer
    permission_classes = []

    def get_queryset(self):
        course_id = self.kwargs["course_id"]
        week_id = self.kwargs["week_id"]
        return Lessons.objects.filter(week_id=week_id, week__course_id=course_id)



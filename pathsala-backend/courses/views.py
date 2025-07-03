from rest_framework import generics, permissions
from enrollments.models import Enrollments
from .models import Courses, Lessons, Videos, Weeks
from .serializers import CourseSerializer, LessonWithVideoIDsSerializer, VideoURLSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

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

class LessonVideoInfoAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, course_id, week_id, lesson_id):
        # Check enrollment
        if not Enrollments.objects.filter(enrolled_student=request.user, course_id=course_id, active=True).exists():
            return Response({'detail': 'Not enrolled in this course.'}, status=status.HTTP_403_FORBIDDEN)
        try:
            lesson = Lessons.objects.get(id=lesson_id, week_id=week_id, week__course_id=course_id)
        except Lessons.DoesNotExist:
            return Response({'detail': 'Lesson not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = LessonWithVideoIDsSerializer(lesson)
        return Response(serializer.data)

class LessonVideoPlayAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, course_id, week_id, lesson_id, video_id):
        # Check enrollment
        if not Enrollments.objects.filter(enrolled_student=request.user, course_id=course_id, active=True).exists():
            return Response({'detail': 'Not enrolled in this course.'}, status=status.HTTP_403_FORBIDDEN)
        try:
            lesson = Lessons.objects.get(id=lesson_id, week_id=week_id, week__course_id=course_id)
        except Lessons.DoesNotExist:
            return Response({'detail': 'Lesson not found.'}, status=status.HTTP_404_NOT_FOUND)
        video = lesson.video
        if not video or video.id != video_id:
            return Response({'detail': 'Video not found for this lesson.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = VideoURLSerializer(video)
        return Response(serializer.data)

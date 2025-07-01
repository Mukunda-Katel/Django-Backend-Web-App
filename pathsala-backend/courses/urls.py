from django.urls import path
from .views import (
    CourseDetailAPIView,
    CourseListAPIView,
    AdminCourseAPIView,
    LessonVideoInfoAPIView,
    LessonVideoPlayAPIView,
)

urlpatterns = [
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('admin/courses/', AdminCourseAPIView.as_view(), name='admin-course'),
    path('courses/<int:course_id>/weeks/<int:week_id>/lessons/<int:lesson_id>/video/', LessonVideoInfoAPIView.as_view(), name='lesson-video-info'),
    path('courses/<int:course_id>/weeks/<int:week_id>/lessons/<int:lesson_id>/video/<int:video_id>/', LessonVideoPlayAPIView.as_view(), name='lesson-video-play'),
]

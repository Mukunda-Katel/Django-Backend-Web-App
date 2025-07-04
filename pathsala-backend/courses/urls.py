from django.urls import path
from .views import CourseListAPIView, AdminCourseAPIView, CourseDetailAPIView, LessonVideoInfoAPIView, LessonVideoPlayAPIView, UpcomingCourseListAPIView, UpcomingCourseDetailAPIView

urlpatterns = [
    path('', CourseListAPIView.as_view(), name='course-list'),
    path('upcoming/', UpcomingCourseListAPIView.as_view(), name='upcoming-course-list'),
    path('upcoming/<int:pk>/', UpcomingCourseDetailAPIView.as_view(), name='upcoming-course-detail'),
    path('admin/', AdminCourseAPIView.as_view(), name='admin-course'),
    path('<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('<int:course_id>/week/<int:week_id>/lesson/<int:lesson_id>/video/', LessonVideoInfoAPIView.as_view(), name='lesson-video-info'),
    path('<int:course_id>/week/<int:week_id>/lesson/<int:lesson_id>/video/<int:video_id>/', LessonVideoPlayAPIView.as_view(), name='lesson-video-play'),
]

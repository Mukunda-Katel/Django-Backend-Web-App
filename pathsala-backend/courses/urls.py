from django.urls import path
from .views import (
    CourseDetailAPIView,
    CourseListAPIView,
    AdminCourseAPIView,
)

urlpatterns = [
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('admin/courses/', AdminCourseAPIView.as_view(), name='admin-course'),
]

from django.urls import path
from .views import PublicCourseListView, PublicCourseDetailView

urlpatterns = [
    path('courses/', PublicCourseListView.as_view(), name='public-course-list'),
    path('courses/<int:pk>/', PublicCourseDetailView.as_view(), name='public-course-detail'),
] 
from django.urls import path
from .views import PublicCourseListView, PublicCourseDetailView, PublicCourseWeeksListView, PublicWeekLessonsListView

urlpatterns = [
    path('courses/', PublicCourseListView.as_view(), name='public-course-list'),
    path('courses/<int:pk>/', PublicCourseDetailView.as_view(), name='public-course-detail'),
    path('courses/<int:course_id>/weeks/', PublicCourseWeeksListView.as_view(), name='public-course-weeks-list'),
    path('courses/<int:course_id>/weeks/<int:week_id>/lessons/', PublicWeekLessonsListView.as_view(), name='public-week-lessons-list'),
] 



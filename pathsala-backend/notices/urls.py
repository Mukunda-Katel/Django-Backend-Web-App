from django.urls import path
from .views import (
    AdminNoticeListCreateAPIView,
    AdminNoticeRetrieveUpdateDestroyAPIView,
    EnrolledUserNotificationListAPIView,
    GlobalNotificationListAPIView,
    UpcomingCourseListCreateAPIView,
    UpcomingCourseNotificationListCreateAPIView,
    UpcomingCourseNotificationDetailAPIView
)

urlpatterns = [
    path('courses/<int:course_id>/notices/', AdminNoticeListCreateAPIView.as_view(), name='notice-list-create'),
    path('notices/<int:pk>/', AdminNoticeRetrieveUpdateDestroyAPIView.as_view(), name='notice-detail'),
    path('notifications/enrolled/', EnrolledUserNotificationListAPIView.as_view(), name='enrolled-notifications'),
    path('notifications/global/', GlobalNotificationListAPIView.as_view(), name='global-notifications'),
    path('upcoming-courses/', UpcomingCourseListCreateAPIView.as_view(), name='upcoming-course-list-create'),
    path('upcoming-course-notifications/', UpcomingCourseNotificationListCreateAPIView.as_view(), name='upcoming-course-notification-list-create'),
    path('upcoming-course-notifications/<int:pk>/', UpcomingCourseNotificationDetailAPIView.as_view(), name='upcoming-course-notification-detail'),
]

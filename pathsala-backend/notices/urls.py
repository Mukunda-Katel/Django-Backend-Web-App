from django.urls import path
from .views import (
    AdminNoticeListCreateAPIView,
    AdminNoticeRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('courses/<int:course_id>/notices/', AdminNoticeListCreateAPIView.as_view(), name='notice-list-create'),
    path('notices/<int:pk>/', AdminNoticeRetrieveUpdateDestroyAPIView.as_view(), name='notice-detail'),
]

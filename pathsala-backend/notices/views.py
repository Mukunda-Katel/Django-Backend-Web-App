from rest_framework import generics, permissions
from .models import Notices, Notification, UpcomingCourse, UpcomingCourseNotification
from .serializers import NoticeSerializer, NotificationSerializer, UpcomingCourseSerializer, UpcomingCourseNotificationSerializer
from enrollments.models import Enrollments
from rest_framework.permissions import IsAuthenticated, AllowAny

class AdminNoticeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Notices.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [permissions.IsAdminUser]

class AdminNoticeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notices.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [permissions.IsAdminUser]

class EnrolledUserNotificationListAPIView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        enrolled_courses = Enrollments.objects.filter(enrolled_student=user, active=True).values_list('course_id', flat=True)
        return Notification.objects.filter(course_id__in=enrolled_courses)

class GlobalNotificationListAPIView(generics.ListAPIView):
    serializer_class = UpcomingCourseNotificationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return UpcomingCourseNotification.objects.all()

class UpcomingCourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = UpcomingCourse.objects.all()
    serializer_class = UpcomingCourseSerializer
    permission_classes = [permissions.IsAdminUser]

class UpcomingCourseNotificationListCreateAPIView(generics.ListCreateAPIView):
    queryset = UpcomingCourseNotification.objects.all()
    serializer_class = UpcomingCourseNotificationSerializer
    permission_classes = [permissions.IsAdminUser]

class UpcomingCourseNotificationDetailAPIView(generics.RetrieveAPIView):
    queryset = UpcomingCourseNotification.objects.all()
    serializer_class = UpcomingCourseNotificationSerializer
    permission_classes = [permissions.AllowAny]
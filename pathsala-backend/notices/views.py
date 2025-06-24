from rest_framework import generics, permissions
from .models import Notices
from .serializers import NoticeSerializer

class AdminNoticeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Notices.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [permissions.IsAdminUser]

class AdminNoticeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notices.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [permissions.IsAdminUser]
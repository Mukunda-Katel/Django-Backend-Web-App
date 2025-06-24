from openai import PermissionDeniedError
from rest_framework import generics, permissions
from .models import LessonResources
from .serializers import LessonResourceSerializer


class LessonResourceListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LessonResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        lesson_id = self.kwargs.get('lesson_id')
        return LessonResources.objects.filter(lesson_id=lesson_id)

    def perform_create(self, serializer):
        # Only allow instructor/admin to upload
        user = self.request.user
        if not user.is_admin:  # or your instructor check
            raise PermissionDeniedError("Only instructors can upload resources.")
        serializer.save()

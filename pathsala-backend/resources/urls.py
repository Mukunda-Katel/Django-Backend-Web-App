from django.urls import path
from .views import (
    LessonResourceListCreateAPIView,
    
)

urlpatterns = [
    path('lessons/<int:lesson_id>/resources/', LessonResourceListCreateAPIView.as_view(), name='lesson-resource-list-create'),
]

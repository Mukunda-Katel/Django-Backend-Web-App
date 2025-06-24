from django.urls import path,include
# from .views import (
#     # QuestionListCreateAPIView,
#     # AnswerListCreateAPIView,
#     # AnswerCommentListCreateAPIView,
#     # QuestionLikeToggleAPIView,
#     # AnswerLikeToggleAPIView,
# )
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet
router = DefaultRouter()
router.register(r'video-comments', CommentViewSet)

urlpatterns = [
    # path('lessons/<int:lesson_id>/questions/', QuestionListCreateAPIView.as_view(), name='questions-list-create'),
    # path('questions/<int:question_id>/answers/', AnswerListCreateAPIView.as_view(), name='answers-list-create'),
    # path('answers/<int:answer_id>/comments/', AnswerCommentListCreateAPIView.as_view(), name='answer-comments-list-create'),
    # path('questions/<int:question_id>/like-toggle/', QuestionLikeToggleAPIView.as_view(), name='question-like-toggle'),
    # path('answers/<int:answer_id>/like-toggle/', AnswerLikeToggleAPIView.as_view(), name='answer-like-toggle'),
    path('',include(router.urls))
]

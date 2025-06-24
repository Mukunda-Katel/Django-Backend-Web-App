from rest_framework import generics, permissions, status
from rest_framework.response import Response
# from .serializers import QuestionSerializer,AnswerSerializer,AnswerCommentSerializer
from rest_framework.exceptions import PermissionDenied
from .models import *
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
# class QuestionListCreateAPIView(generics.ListCreateAPIView):
#     serializer_class = QuestionSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         lesson_id = self.kwargs.get('lesson_id')
#         return Questions.objects.filter(lesson_id=lesson_id)

#     def perform_create(self, serializer):
#         serializer.save(asked_by=self.request.user)


# class AnswerListCreateAPIView(generics.ListCreateAPIView):
#     serializer_class = AnswerSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         question_id = self.kwargs.get('question_id')
#         return Answers.objects.filter(question_id=question_id)

#     def perform_create(self, serializer):
#         serializer.save(answered_by=self.request.user)


# class AnswerCommentListCreateAPIView(generics.ListCreateAPIView):
#     serializer_class = AnswerCommentSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         answer_id = self.kwargs.get('answer_id')
#         return AnswerComments.objects.filter(answer_id=answer_id)

#     def perform_create(self, serializer):
#         serializer.save(commented_by=self.request.user)


# class QuestionLikeToggleAPIView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, question_id):
#         user = request.user
#         question = get_object_or_404(Questions, id=question_id)
#         liked = QuestionLikes.objects.filter(question=question, liked_by=user).first()

#         if liked:
#             liked.delete()
#             return Response({'detail': 'Like removed'}, status=status.HTTP_200_OK)
#         else:
#             QuestionLikes.objects.create(question=question, liked_by=user)
#             return Response({'detail': 'Liked'}, status=status.HTTP_201_CREATED)


# class AnswerLikeToggleAPIView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, answer_id):
#         user = request.user
#         answer = get_object_or_404(Answers, id=answer_id)
#         liked = AnswerLikes.objects.filter(answer=answer, liked_by=user).first()

#         if liked:
#             liked.delete()
#             return Response({'detail': 'Like removed'}, status=status.HTTP_200_OK)
#         else:
#             AnswerLikes.objects.create(answer=answer, liked_by=user)
#             return Response({'detail': 'Liked'}, status=status.HTTP_201_CREATED)

from django.db.models import Prefetch
from rest_framework import status, viewsets, permissions, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import CommentSerializer
class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    print("This is called")
    
    queryset = Comment.objects.none()
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        print("This is query_params",self.request.query_params)
        video_id = self.request.query_params.get('video')
        if not video_id:
            return Comment.objects.none()

        return Comment.objects.filter(
            video_id=video_id,
            parent=None
        ).select_related('user').prefetch_related(
            Prefetch('votes', queryset=Vote.objects.select_related('user')),
            Prefetch('replies', queryset=Comment.objects.select_related('user').prefetch_related(
                Prefetch('votes', queryset=Vote.objects.select_related('user')),
                Prefetch('replies', queryset=Comment.objects.select_related('user').prefetch_related(
                    Prefetch('votes', queryset=Vote.objects.select_related('user'))
                ))
            ))
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def upvote(self, request, pk=None):
        comment = self.get_object()
        vote_value = 1
        
        vote, created = Vote.objects.get_or_create(
            user=request.user, 
            comment=comment,
            defaults={'vote_value': vote_value}
        )
        
        if not created:
            # User already voted, update their vote
            if vote.vote_value == vote_value:
                # User is trying to upvote again, remove the vote
                vote.delete()
                return Response({'status': 'vote_removed'}, status=status.HTTP_200_OK)
            else:
                # User is changing their vote from downvote to upvote
                vote.vote_value = vote_value
                vote.save()
                return Response({'status': 'vote_updated'}, status=status.HTTP_200_OK)
        
        return Response({'status': 'upvoted'}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def downvote(self, request, pk=None):
        comment = self.get_object()
        vote_value = -1
        
        vote, created = Vote.objects.get_or_create(
            user=request.user, 
            comment=comment,
            defaults={'vote_value': vote_value}
        )
        
        if not created:
            # User already voted, update their vote
            if vote.vote_value == vote_value:
                # User is trying to downvote again, remove the vote
                vote.delete()
                return Response({'status': 'vote_removed'}, status=status.HTTP_200_OK)
            else:
                # User is changing their vote from upvote to downvote
                vote.vote_value = vote_value
                vote.save()
                return Response({'status': 'vote_updated'}, status=status.HTTP_200_OK)
        
        return Response({'status': 'downvoted'}, status=status.HTTP_201_CREATED)

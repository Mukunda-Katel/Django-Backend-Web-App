from rest_framework import serializers
# from .models import QuestionLikes,Questions,AnswerComments,AnswerLikes,Answers
from .models import Comment,Vote
# class QuestionSerializer(serializers.ModelSerializer):
#     likes_count = serializers.IntegerField(source='likes.count', read_only=True)
#     class Meta:
#         model = Questions
#         fields = ['id', 'lesson', 'asked_by', 'question_text', 'created_at', 'likes_count']


# class AnswerSerializer(serializers.ModelSerializer):
#     likes_count = serializers.IntegerField(source='likes.count', read_only=True)
#     comments = serializers.StringRelatedField(many=True, read_only=True)

#     class Meta:
#         model = Answers
#         fields = ['id', 'question', 'answered_by', 'answer_text', 'created_at', 'likes_count', 'comments']


# class AnswerCommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AnswerComments
#         fields = ['id', 'answer', 'commented_by', 'comment_text', 'created_at']


# class QuestionLikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = QuestionLikes
#         fields = ['id', 'question', 'liked_by']


# class AnswerLikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AnswerLikes
#         fields = ['id', 'answer', 'liked_by']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    text = serializers.CharField(source='content')
    likes_count = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'likes_count', 'replies']

    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True, context=self.context).data
        return []

    def get_likes_count(self, obj):
        """Calculate total vote score (upvotes - downvotes)"""
        upvotes = obj.votes.filter(vote_value=1).count()
        downvotes = obj.votes.filter(vote_value=-1).count()
        return upvotes - downvotes 
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from courses.models import Lessons
from courses.models import Courses
User = get_user_model()
# class Questions(models.Model):
#     lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name='questions')
#     asked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
#     question_text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Q by {self.asked_by.username} on {self.lesson.title}"


# class Answers(models.Model):
#     question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='answers')
#     answered_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
#     answer_text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"A by {self.answered_by.username} to Q#{self.question.id}"


# class AnswerComments(models.Model):
#     answer = models.ForeignKey(Answers, on_delete=models.CASCADE, related_name='comments')
#     commented_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_comments')
#     comment_text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Comment by {self.commented_by.username} on Answer#{self.answer.id}"


# class QuestionLikes(models.Model):
#     question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='likes')
#     liked_by = models.ForeignKey(User, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ('question', 'liked_by')  # user can like question only once

#     def __str__(self):
#         return f"{self.liked_by.username} liked Q#{self.question.id}"


# class AnswerLikes(models.Model):
#     answer = models.ForeignKey(Answers, on_delete=models.CASCADE, related_name='likes')
#     liked_by = models.ForeignKey(User, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ('answer', 'liked_by')  # user can like answer only once

#     def __str__(self):
#         return f"{self.liked_by.username} liked A#{self.answer.id}"


class Comment(models.Model):
    """
    Stores comments on course videos (supports replies), including user, content, parent comment, and timestamps.
    """
    # The video this comment is for
    video = models.ForeignKey(Lessons, related_name='comments', on_delete=models.CASCADE)
    # The user who made the comment
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    # If this is a reply, the parent comment
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Show username and a snippet of the comment
        return f"{self.user.username}: {self.content[:30]}"

    class Meta:
        ordering = ['created_at'] 

# This model stores votes on comments (upvote/downvote)
class Vote(models.Model):
    """
    Stores a vote on a comment by a user (upvote or downvote).
    """
    VOTE_CHOICES = [
        (1, 'Upvote'),
        (-1, 'Downvote'),
    ]
    
    user = models.ForeignKey(User, related_name='comment_votes', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='votes', on_delete=models.CASCADE)
    vote_value = models.IntegerField(choices=VOTE_CHOICES)  # 1 for upvote, -1 for downvote
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'comment')  # One vote per user per comment
        ordering = ['-created_at']

    def __str__(self):
        vote_type = "upvoted" if self.vote_value == 1 else "downvoted"
        return f'{self.user.username} {vote_type} "{self.comment.content[:20]}"' 
    
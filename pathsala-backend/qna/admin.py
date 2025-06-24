from django.contrib import admin
# from .models import QuestionLikes,Questions,AnswerComments,AnswerLikes,Answers
# Register your models here.
from .models import Comment,Vote
# admin.site.register(QuestionLikes)
# admin.site.register(Questions)
# admin.site.register(AnswerComments)
# admin.site.register(Answers)
# admin.site.register(AnswerLikes)

admin.site.register(Comment)
admin.site.register(Vote)
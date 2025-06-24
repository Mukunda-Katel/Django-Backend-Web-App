# from django.db import models
# from django.conf import settings
# from django.contrib.auth.models import User
# from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True,max_length=100,blank=False)
    username = models.CharField(unique=False,max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

# # class Categorys(models.Model):
# #     category_title = models.CharField(max_length=100)
# #     slug = models.CharField(max_length=100)

# #     def __str__(self):
# #         return f"category-{self.category_title}"
# # class Courses(models.Model):
# #     title = models.CharField(max_length=200)
# #     description = models.TextField()
# #     creator = models.CharField(max_length=100)
# #     price = models.DecimalField(max_digits=8, decimal_places=2, default=1000)
# #     created_at = models.DateTimeField(auto_now_add=True)
# #     category = models.ForeignKey(Categorys,on_delete=models.CASCADE)
# #     duration = models.CharField(max_length=100,default=2)

# #     def __str__(self):
# #         return self.title

# # class Weeks(models.Model):
# #     course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='weeks')
# #     number = models.PositiveIntegerField() 
# #     title = models.CharField(max_length=200, blank=True)

# #     class Meta:
# #         unique_together = ('course', 'number')
# #         ordering = ['number']

# #     def __str__(self):
# #         return f"Week {self.number} - {self.title or ''}"

# # class Lessons(models.Model):
# #     week = models.ForeignKey(Weeks, on_delete=models.CASCADE, related_name='lessons')
# #     title = models.CharField(max_length=200)
# #     description = models.TextField(blank=True)
# #     video_url = models.URLField() 
# #     order = models.PositiveIntegerField()  

# #     class Meta:
# #         unique_together = ('week', 'order')
# #         ordering = ['order']

# #     def __str__(self):
# #         return self.title


# # class Enrollments(models.Model):
# #     enrolled_student = models.ForeignKey(User,on_delete=models.CASCADE,related_name='enrollments')
# #     course = models.ForeignKey(Courses,on_delete=models.CASCADE,related_name='enrollments')
# #     enrolled_at = models.DateTimeField(auto_now_add=True)

# #     active = models.BooleanField(default=True)
# #     progress = models.DecimalField(max_digits=5,decimal_places=2,default=0)

# #     class Meta:
# #         unique_together = ('enrolled_student', 'course')

# #     def __str__(self):
# #         return f"{self.enrolled_student} enrolled in {self.course}"

# class Certificates(models.Model):
#     enrollment = models.OneToOneField('Enrollments', on_delete=models.CASCADE, related_name='certificate')
#     issued_at = models.DateTimeField(default=timezone.now)
#     # certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
#     def __str__(self):
#         return f"Certificate for {self.enrollment.enrolled_student.username} - {self.enrollment.course.title}"



# class Notices(models.Model):
#     notice_title = models.CharField(max_length=100)
#     notice_description = models.TextField()
#     notice_issued = models.CharField(max_length=100)
#     enrolled_course = models.ForeignKey(Courses,on_delete=models.CASCADE,blank=True)

# class Questions(models.Model):
#     lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name='questions')
#     asked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
#     question_text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Q by {self.asked_by.username} on {self.lesson.title}"
    

# class Answers(models.Model):
#     question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='answers')
#     answered_by = models.CharField(max_length=100)
#     answer_text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"A by {self.answered_by.username} to Q#{self.question.id}"

# class LessonResources(models.Model):
#     lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name='resources')
#     title = models.CharField(max_length=200)
#     # file = models.FileField(upload_to='lesson_resources/', blank=True, null=True)
#     external_link = models.URLField(blank=True, null=True)
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Resource for {self.lesson.title}: {self.title}"


# class AnswerComments(models.Model):
#     answer = models.ForeignKey(Answers, on_delete=models.CASCADE, related_name='comments')
#     commented_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_comments')
#     comment_text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Comment by {self.commented_by.username} on Answer #{self.answer.id}"


# class QuestionUpvotes(models.Model):
#     question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='upvotes')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('question', 'user')

#     def __str__(self):
#         return f"{self.user.username} upvoted Question #{self.question.id}"


# class AnswerUpvotes(models.Model):
#     answer = models.ForeignKey(Answers, on_delete=models.CASCADE, related_name='upvotes')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('answer', 'user')

#     def __str__(self):
#         return f"{self.user.username} upvoted Answer #{self.answer.id}"
from django.db import models
from courses.models import Courses
from django.utils import timezone
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class Enrollments(models.Model):
    enrolled_student = models.ForeignKey(User,on_delete=models.CASCADE,related_name='enrollments')
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)
    progress = models.DecimalField(max_digits=5,decimal_places=2,default=0)

    class Meta:
        unique_together = ('enrolled_student', 'course')

    def __str__(self):
        return f"{self.enrolled_student} enrolled in {self.course}"

class Certificates(models.Model):
    enrollment = models.OneToOneField('Enrollments', on_delete=models.CASCADE, related_name='certificate')
    issued_at = models.DateTimeField(default=timezone.now)
    # certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
    def __str__(self):
        return f"Certificate for {self.enrollment.enrolled_student.username} - {self.enrollment.course.title}"
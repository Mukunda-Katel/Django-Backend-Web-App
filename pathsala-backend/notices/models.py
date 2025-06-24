from django.db import models
from courses.models import Courses
# Create your models here.
class Notices(models.Model):
    notice_title = models.CharField(max_length=100)
    notice_description = models.TextField()
    notice_issued = models.CharField(max_length=100)
    enrolled_course = models.ForeignKey(Courses,on_delete=models.CASCADE,blank=True)
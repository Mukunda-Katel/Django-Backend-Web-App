from django.db import models
from courses.models import Lessons

# Create your models here.
class LessonResources(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name='resources')
    title = models.CharField(max_length=200)
    # file = models.FileField(upload_to='lesson_resources/', blank=True, null=True)
    external_link = models.URLField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resource for {self.lesson.title}: {self.title}"
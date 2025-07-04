from django.db import models
from courses.models import Courses
# Create your models here.
class Notices(models.Model):
    notice_title = models.CharField(max_length=100)
    notice_description = models.TextField()
    notice_issued = models.CharField(max_length=100)
    enrolled_course = models.ForeignKey(Courses,on_delete=models.CASCADE,blank=True)

class UpcomingCourse(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

class UpcomingCourseNotification(models.Model):
    upcoming_course = models.ForeignKey(UpcomingCourse, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Upcoming: {self.upcoming_course.title} - {self.message[:30]}"

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('resource', 'Resource Added'),
        ('video', 'Video Uploaded'),
        ('note', 'Note Added'),
        ('new_course', 'New Course'),
        # ('upcoming_course', 'Upcoming Course'),  # Removed
    ]
    type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, blank=True)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    # Optionally: user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.get_type_display()}: {self.message[:30]}"
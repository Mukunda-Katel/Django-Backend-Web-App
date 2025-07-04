from django.contrib import admin
from .models import Notices, Notification, UpcomingCourse, UpcomingCourseNotification

admin.site.register(Notices)
admin.site.register(Notification)
admin.site.register(UpcomingCourse)
admin.site.register(UpcomingCourseNotification)
# Register your models here.

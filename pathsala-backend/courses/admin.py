from django.contrib import admin
from .models import Categorys,Courses,Lessons,Weeks
# Register your models here.
admin.site.register(Categorys)
admin.site.register(Courses)
admin.site.register(Lessons)
admin.site.register(Weeks)
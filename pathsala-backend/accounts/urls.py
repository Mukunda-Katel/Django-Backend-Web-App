from django.urls import path
from . import views
# from .views import (
#     CourseListAPIView,
#     CourseDetailAPIView,
#     AdminCourseAPIView,
#     EnrollApi,
#     CertificateApi
# )
from .views import AboutUser

urlpatterns = [
    # path("",views.home,name='home'),
    path("user/",AboutUser.as_view())
]

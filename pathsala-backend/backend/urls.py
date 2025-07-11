"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from accounts.views import GoogleAuthView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('', admin.site.urls),
    path('qna/', include('qna.urls')),          # QnA app URLs
    path('courses/', include('courses.urls')),  # Courses app URLs
    path('notices/', include('notices.urls')),  # Notices app URLs
    path('enrollment/', include('enrollments.urls')),  # Certificates app URLs
    path('resources/', include('resources.urls')),
    path("auth/",include('social_django.urls',namespace='social')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('google/',GoogleAuthView.as_view(),name='logout'),
    path('accounts/',include('accounts.urls')),
    path('public/', include('non_auth_content.urls')),  # Non-authenticated content URLs
    # path('auth/google/', GoogleLogin.as_view(), name='google-login')
]

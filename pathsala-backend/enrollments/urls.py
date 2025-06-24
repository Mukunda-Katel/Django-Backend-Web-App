from django.urls import path
from .views import (
    AdminCertificateListCreateAPIView,
    EnrollApi,
    AdminCertificateRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # Student enroll API
    path('enroll/', EnrollApi.as_view(), name='enroll'),

    # Admin - issue/view certificates
    path('admin/certificates/', AdminCertificateListCreateAPIView.as_view(), name='admin-certificate-list-create'),
    path('admin/certificates/<int:pk>/', AdminCertificateRetrieveUpdateDestroyAPIView.as_view(), name='admin-certificate-detail'),
]

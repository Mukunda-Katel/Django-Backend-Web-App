from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Enrollments, Certificates
from .serializers import EnrolledCourseSerializer, CertificateSerializer
from rest_framework import generics, permissions
from .models import Certificates
from .serializers import CertificateSerializer
class EnrollApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        enrollments = Enrollments.objects.filter(enrolled_student=user)
        serializer = EnrolledCourseSerializer(enrollments, many=True, context={"request": request})
        return Response(serializer.data)




class AdminCertificateListCreateAPIView(generics.ListCreateAPIView):
    queryset = Certificates.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAdminUser]

class AdminCertificateRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificates.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAdminUser]

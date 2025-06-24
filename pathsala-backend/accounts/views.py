from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
import google.oauth2.id_token
import google.auth.transport.requests
from django.conf import settings
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# from dotenv import load_dotenv
# User = get_user_model()
# import os
# load_dotenv()
# GOOGLE_CLIENT_ID = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
class GoogleAuthView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        id_token = request.data.get('id_token')
        if not id_token:
            return Response({'error': 'No token provided'}, status=400)

        try:
            # Verify token
            request_adapter = google.auth.transport.requests.Request()
            idinfo = google.oauth2.id_token.verify_oauth2_token(
                id_token, request_adapter, audience="337899844345-5qrjsjkrgs9cibgr3sdc4o9rmm1t5arv.apps.googleusercontent.com"
            )

            email = idinfo.get('email')
            name = idinfo.get('name')

            user, _ = User.objects.get_or_create(email=email, defaults={"first_name": name})
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'first_name':name,
                'email':email,
            })
        except Exception as e:
            return Response({'error': 'Invalid token', 'details': str(e)}, status=400)


class AboutUser(APIView):
    def get(self,request):
        user = request.user
        # print("this is user",u)
        print("This is user", user)
        serializer = UserSerializer(user)
        return Response(serializer.data)
        # return Response(serializer.errors)
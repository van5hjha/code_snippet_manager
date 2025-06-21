from .serializers import UserModelSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

class RegisterView(generics.CreateAPIView):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

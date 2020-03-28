from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
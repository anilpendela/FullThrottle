from rest_framework import routers, serializers, viewsets
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['real_name', 'user_id', 'tz', 'activity_periods']
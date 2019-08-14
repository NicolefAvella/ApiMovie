from rest_framework import serializers
from user.models import User

class TokenSerializer(serializers.Serializer):
    """This serializer serializes the token data"""
    token = serializers.CharField(max_length=255)

class UserSerializer(serializers.ModelSerializer):
    """User model serializer"""

    class Meta:
        model = User
        fields = (
           'username',
           'first_name',
           'email',
        )

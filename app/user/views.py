from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

#serializers
from user.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer,
)

class UserLoginAPIView(APIView):
    """User login API view"""

    def post(self, request, *args, **kwargs):
        """HTTP POST request"""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        data = {
            'user':UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

class UserSignUpAPIView(APIView):
    """User Signup API view"""

    def post(self, request, *args, **kwargs):
        """HTTP POST request"""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
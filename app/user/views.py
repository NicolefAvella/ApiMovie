from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions

from user.models import User
from django.contrib.auth import authenticate, login

#serializers
from user.serializers import UserSerializer, BlackSerializer


# Get the JWT settings, add these lines after the import/from lines
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserLoginAPIView(generics.CreateAPIView):
    #User login API view"""

    permission_classes = (permissions.AllowAny,)

    #queryset = User.objects.all()

    #TODO : ERASER
    """def post(self, request, *args, **kwargs):
        #HTTP POST request

        username = request.data.get("username", "")
        password = request.data.get("password", "")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)"""


class RegisterUsers(generics.CreateAPIView):
    """ POST register user """
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

class BlackList(generics.CreateAPIView):
    """Archive token for user, invalidate token"""
    serializer_class = BlackSerializer

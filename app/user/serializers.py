from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from django.contrib.auth import authenticate, password_validation

from user.models import User, Profile


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer"""

    class Meta:
        model = User
        fields = (
           'username',
           'first_name',
           'email',
        )

class UserSignUpSerializer(serializers.Serializer):
    """User Sign Up serializer"""

    email = serializers.EmailField(
       validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
       min_length=6,
       validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8, max_length=10)
    password_confirmation = serializers.CharField(min_length=8, max_length=10)

    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)

    def validate(self, data):
        """Verify password"""
        passw = data['password']
        pass_confirm = data['password_confirmation']
        if passw != pass_confirm:
            raise serializers.ValidationError("Error password")
        password_validation.validate_password(passw)
        return data

    def create(self, data):

        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile.objects.create(user=user)
        return user

class UserLoginSerializer(serializers.Serializer):
    """User login serializer"""

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Check credentials"""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializer.ValidationError('Invalid credentials')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generate or retrieve token"""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key

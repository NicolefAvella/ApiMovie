from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from user.models import User, BlackListedToken

class TokenSerializer(serializers.Serializer):
    """This serializer serializes the token data"""
    token = serializers.CharField(max_length=255)
    # TODO: delete

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
        min_length=4,
        required=True
    )
    first_name = serializers.CharField(
        min_length=4,
        required=True
    )

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ( 'id', 'email', 'password', 'username', 'first_name', 'last_name')

class BlackSerializer(serializers.ModelSerializer):
    """Serializer for invalid token"""

    def create(self, validated_data):
        instance = BlackListedToken.objects.create(
            token=validated_data['token'],
            user=self.context['request'].user
        )
        instance.save()

        return instance


    class Meta:
        model = BlackListedToken
        fields = ('token')

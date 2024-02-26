from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from . models import User

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "name", "last_name", "password"]

class MyTokerObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email
        token['avatar'] = user.avatar.url
        token['is_staff'] = user.is_staff

        return token
        
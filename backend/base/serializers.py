from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import ArtUpload

# ✅ User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]

# ✅ Registration Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# ✅ Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

# ✅ Art Upload Serializer
class ArtUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtUpload
        fields = ["id", "user", "image", "description"]
        extra_kwargs = {"user": {"read_only": True}}

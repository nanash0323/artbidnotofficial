from rest_framework import serializers
from .models import CustomUser, ArtUpload, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class ArtUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtUpload
        fields = ["id", "uploaded_by", "image", "description"]
        extra_kwargs = {"uploaded_by": {"read_only": True}}
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Include all fields from the Product model

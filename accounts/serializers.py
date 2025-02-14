from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['phone_number', 'username', 'password', 'membership_type']

    def create(self, validated_data):
        # Generate a default username using phone_number if not provided
        if not validated_data.get("username"):
            validated_data["username"] = validated_data["phone_number"]
            
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password"
        ]

    def create(self, validated_data):

        password = validated_data.pop("password")

        user = User(**validated_data)

        user.set_password(password)

        user.role = "customer"

        user.save()

        return user

class LoginSerializer(serializers.Serializer):

    identifier = serializers.CharField()

    password = serializers.CharField(
        write_only=True
    )

    def validate(self, attrs):

        identifier = attrs.get("identifier")
        password = attrs.get("password")

        user = None

        if "@" in identifier:

            try:
                user = User.objects.get(
                    email=identifier
                )
            except User.DoesNotExist:
                pass

        else:

            try:
                user = User.objects.get(
                    username=identifier
                )
            except User.DoesNotExist:
                pass

        if not user:
            raise serializers.ValidationError(
                "Invalid credentials"
            )

        if not user.check_password(password):
            raise serializers.ValidationError(
                "Invalid credentials"
            )

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role
            }
        }
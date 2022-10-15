from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from projects.models import Project
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'email': {'required': True},
            'password': {'required': True},
            'password2': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class UserProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["title", "description"]


class UserDetailsSerializer(serializers.ModelSerializer):
    projects = UserProjectsSerializer(many=True, read_only=True)
    developer_in_projects = UserProjectsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["last_login", "first_name", "last_name", "email", "projects", "developer_in_projects",
                  "tasks", "date_joined", "updated_at"]

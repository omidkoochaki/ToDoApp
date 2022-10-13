from django.shortcuts import render

from rest_framework import generics, viewsets, mixins, permissions
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet, ModelViewSet

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )

from users.models import User
from users.serializers import RegisterSerializer, UserDetailsSerializer


class RegisterView(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserDetailViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin,):
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserDetailsSerializer



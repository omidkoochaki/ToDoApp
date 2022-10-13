from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from core.models import BaseModel


class MyUserManager(UserManager):

    def create_superuser(self, email=None, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        username = email
        return super().create_user(username, email, password, **extra_fields)


class User(AbstractUser, BaseModel):
    username = None
    USERNAME_FIELD = 'email'

    email = models.EmailField(max_length=254, unique=True)
    is_manager = models.BooleanField(default=False)
    is_developer = models.BooleanField(default=True)

    REQUIRED_FIELDS = []

    objects = MyUserManager()

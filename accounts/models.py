from django.contrib.auth.models import UserManager
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('vous devez entrer une adresse email.')
        email = self.normalize_email(email)
        user = self.normalize_email(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_super_user(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        blank=False,
        max_length=255
    )
    is_active = models.BooleanField(default=True),
    is_staff = models.BooleanField(default=False),
    is_admin = models.BooleanField(default=False)

    zip_code = models.CharField(max_length=5, blank=False)

    USERNAME_FIELD = "email"
    objects = UserManager()

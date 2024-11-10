from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager
from django.utils import timezone


# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    profile_completed = models.BooleanField(default=False)
    role = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=50, null=True)
    facility_name = models.CharField(max_length=100, null=True)
    is_approved = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
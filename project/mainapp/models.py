from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group
from django.contrib.auth.models import UserManager
from django.db.models.deletion import CASCADE
from rest_framework import serializers
import uuid

from django.utils import timezone
# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(
        verbose_name='email address',
        blank=False,
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=150, blank=False, unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_email_verified = models.BooleanField(default=False, blank=False)
    groups = models.ManyToManyField(Group, blank=False)
    objects = UserManager()
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']
    


class UserVerification(models.Model):
    token = models.CharField(max_length=150, default = uuid.uuid4)
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    is_used = models.BooleanField()

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=150)

    class Meta:
        model = CustomUser
        #
        fields = ['pk','email','username','first_name','last_name','password']

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.contrib.auth.base_user import BaseUserManager
from apps.core.models import AbstractBaseModel


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email or not password:
            raise ValueError('User must have an email address and password')

        email = email.lower()
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        email = email.lower()
        user = self.create_user(email, password=password)
        user.is_staff, user.is_superuser, user.is_active = True, True, True
        user.save()
        return user

    def get_by_natural_key(self, username):
        return self.get(email__iexact=username)


class User(AbstractUser, AbstractBaseModel):
    email = models.EmailField(max_length=255, unique=True, )
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    password = models.CharField(max_length=125, null=True)
    coins = models.IntegerField(default=0)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class ScheduledReward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    execute_at = models.DateTimeField()


class RewardLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    given_at = models.DateTimeField(auto_now_add=True)

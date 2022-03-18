from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField()
    birthday = models.DateField()
    mobile = models.CharField()
    gender = models.CharField()
    email = models.CharField()

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __str__(self):
        return self.name
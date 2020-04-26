from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=10)
    user_phone = models.CharField(max_length=12)
    user_zipcode = models.CharField(max_length=6)


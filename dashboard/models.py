from django.db import models
from users.models import CustomUser


class RequestLocation(models.Model):
    requestlocation_id = models.AutoField(primary_key=True)
    requestlocation_latitude = models.DecimalField(decimal_places=6, max_digits=12)
    requestlocation_longitude = models.DecimalField(decimal_places=6, max_digits=12)


class UserRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=15, choices=(('food', 'Food'), ('mask', 'Mask'), ('baby', 'Baby-sitting')))
    request_location = models.ForeignKey(RequestLocation, on_delete=models.CASCADE)
    received_help = models.BooleanField(default=False)

from django.db import models
from user.models import User
from seat.models import Seat

# Create your models here.
class Schedule(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ManyToManyField(Seat)

    class Meta:
        app_label = 'schedule'
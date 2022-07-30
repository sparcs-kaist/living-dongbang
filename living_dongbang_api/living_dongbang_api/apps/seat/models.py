from django.db import models

# Create your models here.
class Seat(models.Model):
    # UUID
    uuid = models.CharField(max_length=36, primary_key=True)

    # array of Schedule associated with one seat
    schedules = models.ManyToManyField('Schedule', related_name='seats')
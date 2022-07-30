from django.db import models

# Create your models here.
class Schedule(models.Model):
    # UUID
    uuid = models.CharField(max_length=36, primary_key=True)
    # UUID of the user
    user_uuid = models.CharField(max_length=36)
    # UUID of the seat associated with the schedule(many-to-many)
    seat_uuid = models.CharField(max_length=36)
    # Starting time in UTC
    start_time = models.DateTimeField()
    # Ending time in UTC
    end_time = models.DateTimeField()
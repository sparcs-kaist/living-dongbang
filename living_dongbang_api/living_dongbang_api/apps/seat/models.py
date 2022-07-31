from django.db import models
class Seat(models.Model):
    # UUID
    code = models.CharField(max_length=20, primary_key=True)
    class Meta:
        app_label = 'seat'

    @property
    def is_available(self):
        return True
 
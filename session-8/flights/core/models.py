from django.db import models

class Flight(models.Model):
    frm = models.CharField(max_length=3)
    to = models.CharField(max_length=3)
    date_time = models.DateField()

    def __str__(self):
        return f"{self.frm} - {self.to}"
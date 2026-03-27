from django.db import models

class Timetable(models.Model):
    day = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day} - {self.subject}"

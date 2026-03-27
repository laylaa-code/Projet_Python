from django.db import models

class Exam(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    date = models.DateField()
    max_marks = models.IntegerField()

    def __str__(self):
        return self.name

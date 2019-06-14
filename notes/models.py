from django.db import models

# class User(models.Model):
#     username = models.CharField(16)
#     password = models.CharField(32)
#
#     def __str__(self):
#         return self.username


class Note(models.Model):
    user = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.text


class LocationLog(models.Model):
    time = models.DateTimeField()

    def __str__(self):
        return self.time


# Create your models here.

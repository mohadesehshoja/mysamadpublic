from django.db import models

from .abstract import TimeStampedModel
from .university import University


class Admin(TimeStampedModel):
    unis = models.ForeignKey(University, on_delete=models.CASCADE, related_name='admin')
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    def __str__(self):
        return "username:{}".format(self.username)


class MyUser(TimeStampedModel):
    unis = models.ForeignKey(University, on_delete=models.CASCADE, related_name='users')
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    def __str__(self):
        return "username:{}".format(self.username)

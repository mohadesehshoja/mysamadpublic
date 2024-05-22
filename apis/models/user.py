from django.db import models
from .university import University
from apis.models.profile import Profile


class User(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    unis = models.ForeignKey(University, on_delete=models.CASCADE, related_name='users')
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    def __str__(self):
        return "username:{}".format(self.username)

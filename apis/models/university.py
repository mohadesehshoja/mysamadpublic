from django.db import models

from apis.models.abstract import BaseModel, TimeStampedModel


class University(TimeStampedModel, BaseModel):
    address = models.TextField()
    phone_number1 = models.CharField(max_length=15)
    phone_number2 = models.CharField(max_length=15, blank=True,null=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)

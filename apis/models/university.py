from django.db import models

from apis.models.abstract import BaseModel


class University(BaseModel):
    address = models.TextField()

    def __str__(self):
        return "{}".format(self.name)

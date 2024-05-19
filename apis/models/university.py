from django.db import models

from apis.models.abstract import BaseModel
from apis.models.restaurant import Restaurant


class Uni(BaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='unis')
    def __str__(self):

        return "{}".format(self.name)
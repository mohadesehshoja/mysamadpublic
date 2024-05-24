from django.db import models

from apis.models.abstract import BasePayment, TimeStampedModel
from apis.models.restaurant import MenuItem
from .user import User


class Reservation(TimeStampedModel, BasePayment):
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='reservations')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')

    def __str__(self):
        return "{}--{}".format(self.user.username, self.menuitem.food.name)

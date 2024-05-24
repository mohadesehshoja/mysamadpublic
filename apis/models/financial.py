from django.db import models

from apis.models.abstract import BasePayment, TimeStampedModel
from .user import User


class Financial(TimeStampedModel, BasePayment):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='financials')

    def __str__(self):
        return "{}".format(self.user.username)

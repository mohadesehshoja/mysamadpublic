from django.db import models

from apis.models.abstract import BasePayment
from apis.models.user import User


class Financial(BasePayment):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='financials', null=True, blank=True)

    def __str__(self):
        return "{}".format(self.user_financial.username)

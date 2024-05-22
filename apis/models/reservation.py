from django.db import models

from apis.models.abstract import BasePayment
from apis.models.restaurant import Food, Menu, Restaurant, Meal, FoodItem
from apis.models.user import User


class Reservation(BasePayment):
    fooditem = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name='reservations', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations', null=True, blank=True)

    def __str__(self):
        return "{}"

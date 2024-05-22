from tkinter import Menu

from django.db import models

from apis.models.abstract import BaseModel
from .university import University


class Restaurant(BaseModel):
    uni = models.ForeignKey(University, on_delete=models.CASCADE, related_name='restaurants', null=True)

    def __str__(self):
        return "Restaurant {}".format(self.name)


class Food(BaseModel):
    pass


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    date = models.DateField()

    def __str__(self):
        return "{}--{}".format(self.restaurant.name, self.date)


class Meal(models.Model):
    lunch = 'lunch'
    dinner = 'dinner'
    choices = ((lunch, 'lunch'), (dinner, 'dinner'))
    meal_type = models.CharField(choices=choices)
    price = models.IntegerField()

    def __str__(self):
        return 'Meal {} - {}'.format(self.meal_type, self.price)


class FoodItem(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='fooditems', null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='fooditems', null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='fooditems', null=True)

    def __str__(self):
        return "{} - {} -{}".format(self.meal.meal_type, self.food.name, self.menu.restaurant.name)

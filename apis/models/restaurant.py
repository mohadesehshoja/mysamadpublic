from django.db import models

from apis.models.abstract import BaseModel, TimeStampedModel
from .university import University


class Restaurant(TimeStampedModel, BaseModel):
    uni = models.ForeignKey(University, on_delete=models.CASCADE, related_name='restaurants')
    address = models.TextField()
    phone = models.CharField(max_length=15)
    opening_hours = models.IntegerField()
    closing_hours = models.IntegerField()

    def __str__(self):
        return "Restaurant {}".format(self.name)


class Food(TimeStampedModel, BaseModel):
    salad = models.CharField(max_length=150, null=True, blank=True)
    drink = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return "{}-{}-{}".format(self.name, self.salad, self.drink)


class Menu(TimeStampedModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    date = models.DateField()

    def __str__(self):
        return "{}--{}".format(self.restaurant.name, self.date)


class Meal(TimeStampedModel):
    breakfast = 'breakfast'
    lunch = 'lunch'
    dinner = 'dinner'
    choices = ((breakfast, 'breakfast'), (lunch, 'lunch'), (dinner, 'dinner'))
    meal_type = models.CharField(choices=choices)
    price = models.IntegerField()

    def __str__(self):
        return '{} - {}'.format(self.meal_type, self.price)


class MenuItem(TimeStampedModel):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='fooditems')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='fooditems')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='fooditems')

    def __str__(self):
        return "{} - {} -{}".format(self.meal.meal_type, self.food.name, self.menu.restaurant.name)

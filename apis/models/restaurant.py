from django.db import models

from apis.models.abstract import BaseModel


class Meal(models.Model):
    lunch = 'lunch'
    dinner = 'dinner'
    choices = ((lunch, 'lunch'), (dinner, 'dinner'))
    meal_type = models.CharField(choices=choices)
    price = models.IntegerField()

    def __str__(self):
        return 'Meal {} - {}'.format(self.meal_type, self.price)



class Food(BaseModel):
    meal = models.ManyToManyField(Meal, related_name='foods')
    date = models.DateField()

    def __str__(self):
        for meals in self.meal.all():
            mymeal = meals.meal_type
        return "Food {} - {} - {}".format(self.name, mymeal, self.date)


class Restaurant(BaseModel):
    food = models.ManyToManyField(Food, related_name='restaurants')

    def __str__(self):
        return "Restaurant {}".format(self.name)

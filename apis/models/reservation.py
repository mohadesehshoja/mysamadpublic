from django.db import models

from apis.models.restaurant import Food


class Reservation(models.Model):
    reservs=models.ManyToManyField(Food,related_name='reservations')
    def __str__(self):
        myfoods="reservs:"
        for food in self.reservs.all():
            myfoods+=food.name
        return "{} ".format(myfoods)



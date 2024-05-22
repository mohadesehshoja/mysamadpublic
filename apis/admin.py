from django.contrib import admin

from apis.models.financial import Financial
from apis.models.profile import Profile
from apis.models.reservation import Reservation
from apis.models.restaurant import Meal, Food, Restaurant, Menu, FoodItem
from apis.models.university import University
from apis.models.user import User

# Register your models here.
admin.site.register(Meal)
admin.site.register(Food)
admin.site.register(Menu)
admin.site.register(FoodItem)
admin.site.register(Restaurant)
admin.site.register(University)
admin.site.register(Reservation)
admin.site.register(Financial)
admin.site.register(Profile)
admin.site.register(User)

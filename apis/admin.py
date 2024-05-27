from django.contrib import admin

from apis.models.financial import Financial
from apis.models.profile import Profile
from apis.models.reservation import Reservation
from apis.models.restaurant import Meal, Food, Restaurant, Menu, MenuItem
from apis.models.university import University
from apis.models.user import MyUser, Admin

# Register your models here.
admin.site.register(Meal)
admin.site.register(Food)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Restaurant)
admin.site.register(University)
admin.site.register(Reservation)
admin.site.register(Financial)
admin.site.register(Profile)
admin.site.register(MyUser)
admin.site.register(Admin)

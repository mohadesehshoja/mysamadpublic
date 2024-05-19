from django.contrib import admin

from apis.models.financial import Financial
from apis.models.reservation import Reservation
from apis.models.restaurant import Meal, Food, Restaurant
from apis.models.university import Uni

# Register your models here.
admin.site.register(Meal)
admin.site.register(Food)
admin.site.register(Restaurant)
admin.site.register(Uni)
admin.site.register(Reservation)
admin.site.register(Financial)
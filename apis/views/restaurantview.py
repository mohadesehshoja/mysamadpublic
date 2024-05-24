from rest_framework import viewsets

from rest_framework.response import Response

from apis.models.restaurant import Restaurant, Food, Meal, MenuItem
from apis.models.restaurant import Menu

from apis.serializations.restaurantserialization import RestaurantSerializer, FoodSerializer, MealSerializer, \
    MenuSerializer, MenuItemSerializer
from module.check import CheckAuthentication


class RestaurantViewSet(viewsets.ViewSet):

    def list(self, request):
        final = []
        token = request.COOKIES.get('token')
        user = CheckAuthentication(token)
        for restaurant in Restaurant.objects.filter(uni__name=user.unis.name):
            data = {
                "id": restaurant.id,
                "created": restaurant.created,
                "modified": restaurant.modified,
                "active": restaurant.active,
                "name": restaurant.name,
                "address": restaurant.address,
                "phone": restaurant.phone,
                "opening_hours": restaurant.opening_hours,
                "closing_hours": restaurant.closing_hours,
                "uni": user.unis.id
            }
            final.append(data)
        return Response(final)

    def create(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class FoodViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Food.objects.all()
        serializer = FoodSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class MealViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Meal.objects.all()
        serializer = MealSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class MenuViewSet(viewsets.ViewSet):
    def list(self, request):
        token = request.COOKIES.get('token')
        user = CheckAuthentication(token)
        final = []
        unis = user.unis
        for item in Restaurant.objects.filter(uni__name=unis):
            for item2 in Menu.objects.filter(restaurant__name=item.name):
                data = {
                    "id": item2.id,
                    "created": item2.created,
                    "modified": item2.modified,
                    "active": item2.active,
                    "date": item2.date,
                    "restaurant": item2.restaurant.id
                }
                final.append(data)
        return Response(final)

    def create(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class MenuItemViewSet(viewsets.ViewSet):
    def list(self, request):
        token = request.COOKIES.get('token')
        user = CheckAuthentication(token)
        unis = user.unis
        final = []
        for item in Restaurant.objects.filter(uni__name=unis):
            for item2 in Menu.objects.filter(restaurant__name=item.name):
                for item3 in MenuItem.objects.filter(menu_id=item2.id):
                    data = {
                        "id": item3.id,
                        "created": item3.created,
                        "modified": item3.modified,
                        "active": item3.active,
                        "meal": item3.meal.id,
                        "food": item3.food.id,
                        "menu": item3.menu.id
                    }
                    final.append(data)
        return Response(final)

    def create(self, request):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

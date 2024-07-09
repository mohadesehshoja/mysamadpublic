from rest_framework import viewsets

from rest_framework.response import Response

from apis.models.restaurant import Restaurant, Food, Meal, MenuItem
from apis.models.restaurant import Menu

from apis.serializations.restaurantserialization import RestaurantSerializer, FoodSerializer, MealSerializer, \
    MenuSerializer, MenuItemSerializer
from module.check import CheckAuthentication, CheckToken


class RestaurantViewSet(viewsets.ViewSet):

    def list(self, request):
        token = request.COOKIES.get('user_token')
        user = CheckAuthentication(token)
        token2 = request.COOKIES.get('admin_token')
        admin = CheckToken(token2)
        if user != False:
            queryset = Restaurant.objects.filter(uni=user.unis)
            serializer = RestaurantSerializer(queryset, many=True)
            return Response(serializer.data)
        elif admin != False:
            queryset = Restaurant.objects.filter(uni=admin.unis)
            serializer = RestaurantSerializer(queryset, many=True)
            return Response(serializer.data)
        return Response("cant access this page")

    def create(self, request):
        token2 = request.COOKIES.get('admin_token')
        admin = CheckToken(token2)
        if admin != False:
            serializer = RestaurantSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response("you must be admin!!!")


class FoodViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Food.objects.all()
        serializer = FoodSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        token2 = request.COOKIES.get('admin_token')
        admin = CheckToken(token2)
        if admin != False:
            serializer = FoodSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response("you must be admin!!!")


class MealViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Meal.objects.all()
        serializer = MealSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        token2 = request.COOKIES.get('admin_token')
        admin = CheckToken(token2)
        if admin != False:
            serializer = MealSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response("you must be admin!!!")


class MenuViewSet(viewsets.ViewSet):
    def list(self, request):
        token = request.COOKIES.get('user_token')
        user = CheckAuthentication(token)
        token2 = request.COOKIES.get('admin_token')
        admin = CheckToken(token2)
        final = []
        if user != False:
            unis = user.unis
            for item in Restaurant.objects.filter(uni__name=unis):
                queryset = Menu.objects.filter(restaurant=item)
                serializer = MenuSerializer(queryset, many=True)
                final.extend(serializer.data)
            return Response(final)
        elif admin != False:
            unis = admin.unis
            for item in Restaurant.objects.filter(uni__name=unis):
                queryset = Menu.objects.filter(restaurant=item)
                serializer = MenuSerializer(queryset, many=True)
                final.extend(serializer.data)
            return Response(final)
        return Response("you must be admin or user!!!")

    def create(self, request):
        token2 = request.COOKIES.get('admin_token')
        admin = CheckToken(token2)
        if admin != False:
            serializer = MenuSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response("you must be admin!!!")


class MenuItemViewSet(viewsets.ViewSet):
    def list(self, request):
        token = request.COOKIES.get('user_token')
        user = CheckAuthentication(token)
        token2 = request.COOKIES.get('admin_token')
        admin = CheckToken(token2)
        if user != False:
            unis = user.unis
            final = []
            for item in Restaurant.objects.filter(uni__name=unis):
                for item2 in Menu.objects.filter(restaurant__name=item.name):
                    queryset = MenuItem.objects.filter(menu=item2)
                    serializer = MenuItemSerializer(queryset, many=True)
                    final.extend(serializer.data)
            return Response(final)
        elif admin != False:
            unis = admin.unis
            final = []
            for item in Restaurant.objects.filter(uni__name=unis):
                for item2 in Menu.objects.filter(restaurant__name=item.name):
                    queryset = MenuItem.objects.filter(menu=item2)
                    serializer = MenuItemSerializer(queryset, many=True)
                    final.extend(serializer.data)
            return Response(final)
        return Response("you must be admin or user!!!")

    def create(self, request):
        token2 = request.COOKIES.get('admin_token')
        admin = CheckToken(token2)
        if admin != False:
            serializer = MenuItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response("you must be admin !!!")

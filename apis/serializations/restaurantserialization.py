from rest_framework import serializers
from rest_framework.templatetags.rest_framework import data

from apis.models.restaurant import Restaurant, Food, Menu, Meal, MenuItem


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

    def validate(self, data):
        if data["opening_hours"] >= 24:
            raise serializers.ValidationError("invalid opening hours")
        if data["closing_hours"] >= 24:
            raise serializers.ValidationError("invalid closing hours")
        if len(data["phone"]) != 11:
            raise serializers.ValidationError("invalid phone number")
        if len(data["phone"]) == 11:
            try:
                int(data["phone"])
            except ValueError:
                raise serializers.ValidationError("invalid phone number type")
        return data


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"

from rest_framework import serializers

from apis.models.financial import Financial
from apis.models.profile import Profile
from apis.models.reservation import Reservation
from apis.models.university import University
from apis.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        if len(data['password']) < 8:
            raise serializers.ValidationError("password must be at least 8 characters long")
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("we have already registered with this username")
        if User.objects.filter(password=data['password']).exists():
            raise serializers.ValidationError("password")
        return data


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', "unis"]


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

    def validate(self, data):
        if len(data["phone_number1"]) != 11:
            raise serializers.ValidationError("invalid phone number")
        if len(data["phone_number1"]) == 11:
            try:
                int(data["phone_number1"])
            except ValueError:
                raise serializers.ValidationError("invalid phone number type")
        if len(data["phone_number2"]) != 11:
            raise serializers.ValidationError("invalid phone number")
        if len(data["phone_number2"]) == 11:
            try:
                int(data["phone_number2"])
            except ValueError:
                raise serializers.ValidationError("invalid phone number type")
        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def validate(self, data):
        if len(data["phone"]) != 11:
            raise serializers.ValidationError("invalid phone number")
        if len(data["phone"]) == 11:
            try:
                int(data["phone"])
            except ValueError:
                raise serializers.ValidationError("invalid phone number type")
        return data


class FinancialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financial
        fields = '__all__'

    def validate(self, data):
        if data['payment_amount'] < 200000:
            raise serializers.ValidationError("you must pay at least 200000")
        return data


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

from rest_framework import serializers

from apis.models.user import Admin


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

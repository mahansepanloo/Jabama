from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import *
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], password=validated_data['password'])
        return user


















class OwnerSerializers(ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"

class BuyerSerializers(ModelSerializer):
    class Meta:
        model = Buyer
        fields = "__all__"


from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User



class UserSerializers(ModelSerializer):
    class Meta:

        model = User
        fields = "__all__"

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        is_staff = validated_data.get('is_staff', False)

        user = User(username=username, is_staff=is_staff)
        user.set_password(password)
        user.save()
        return user
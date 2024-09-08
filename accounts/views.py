from django.contrib.auth.models import User
from rest_framework import generics
from . import serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


class Login(TokenObtainPairView):
    """
    View for user login. Inherits from TokenObtainPairView to handle
    user authentication and token generation.
    """
    pass


class Refresh(TokenRefreshView):
    """
    View for refreshing JWT tokens. Inherits from TokenRefreshView to
    handle token refresh requests.
    """
    pass


class ShowListUser(generics.ListAPIView):
    """
    View to list all users. Accessible only to authenticated users
    with admin permissions. Uses UserSerializers for serialization.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializers
    permission_classes = [IsAuthenticated, IsAdminUser]


class ShowInfoUser(generics.ListAPIView):
    """
    View to retrieve the authenticated user's information. Requires
    authentication. Uses UserSerializers for serialization.
    """
    serializer_class = serializers.UserSerializers
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return User.objects.filter(username=self.request.user)


class CreateUser(generics.CreateAPIView):
    """
    View to create a new user. Uses UserSerializers for serialization.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializers


class Edit(generics.UpdateAPIView):
    """
    View to edit an existing user's information. Requires authentication.
    Uses UserSerializers for serialization.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializers
    permission_classes = [IsAuthenticated]


class DeletUser(generics.DestroyAPIView):
    """
    View to delete a user. Accessible only to authenticated users
    with admin permissions. Uses UserSerializers for serialization.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializers
    permission_classes = [IsAuthenticated, IsAdminUser]
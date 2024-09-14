from django.contrib.auth.models import User
from rest_framework import generics
from . import serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Owner,Buyer
from rest_framework import status
from django.db import transaction


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
    serializer_class = serializers.BuyerSerializers
    permission_classes = [IsAuthenticated, IsAdminUser]


class ShowInfoUser(generics.ListAPIView):
    """
    View to retrieve the authenticated user's information. Requires
    authentication. Uses UserSerializers for serialization.
    """
    serializer_class = serializers.BuyerSerializers
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return User.objects.filter(username=self.request.user)


class CreateUser(APIView):
    """
    View to create a new user.
    """
    def post(self, request):
        try:

            with transaction.atomic():
                    data = request.data
                    users_serializer = serializers.UserSerializer(data=data)
                    if users_serializer.is_valid():
                            user = users_serializer.save()
                    else:
                        return Response({"error": "Invalid user provided."}, status=status.HTTP_400_BAD_REQUEST)

                    role = data.get('rol')
                    if role == "owner":
                                Owner.objects.create(user=user)
                    elif role == "buyer":
                                Buyer.objects.create(user=user)
                    else:
                            return Response({"error": "Invalid role provided."}, status=status.HTTP_400_BAD_REQUEST)

                    return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Edit(generics.UpdateAPIView):
    """
    View to edit an existing user's information. Requires authentication.
    Uses UserSerializers for serialization.
    """
    queryset = User.objects.all()
    serializer_class = serializers.BuyerSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Buyer.objects.filter(user=self.request.user)


class DeletUser(generics.DestroyAPIView):
    """
    View to delete a user. Accessible only to authenticated users
    with admin permissions. Uses UserSerializers for serialization.
    """
    queryset = User.objects.all()
    serializer_class = serializers.BuyerSerializers
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Buyer.objects.filter(user=self.request.user)

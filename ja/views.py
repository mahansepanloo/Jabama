from .serializers import JaSerializers, RateSerializers
from rest_framework import generics
from .models import Ja, Rate
from rest_framework.permissions import IsAuthenticated
from accounts.models import Owner
from rest_framework.exceptions import NotFound


class ListJa(generics.ListCreateAPIView):
    queryset = Ja.objects.filter(confirmation=True)
    serializer_class = JaSerializers


    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [IsAuthenticated]
        return super(ListJa, self).get_permissions()



    def perform_create(self, serializer):
        try:
            owner = Owner.objects.get(user=self.request.user)
            serializer.save(owner=owner)
        except Owner.DoesNotExist:
            raise NotFound("Owner instance does not exist for this user.")


class Rateing(generics.ListCreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(users=self.request.user)


class InfoJa(generics.RetrieveAPIView):
    queryset = Ja.objects.all()
    serializer_class = JaSerializers






class ManageJa(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ja.objects.all()
    serializer_class = JaSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ja.objects.filter(owner__user = self.request.user)






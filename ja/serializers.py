from rest_framework.serializers import ModelSerializer
from .models import Ja, Rate



class JaSerializers(ModelSerializer):
    class Meta:

        model = Ja
        exclude  = ['owner']

    def get_total_rate(self, obj):
        return obj.total_rate()


class RateSerializers(ModelSerializer):
    class Meta:
        model = Rate
        fields = "__all__"


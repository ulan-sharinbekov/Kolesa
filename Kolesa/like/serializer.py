from rest_framework import serializers
from like.models import Like
from api.serializers import CarSerializer

class LikeFullSerializer(serializers.Serializer):
    pass


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
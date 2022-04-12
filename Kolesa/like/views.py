
from django.shortcuts import render
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from like.models import Like
from like.serializer import LikeFullSerializer, LikeSerializer


class LikeViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == "GET":
           return LikeFullSerializer
        else:
            return LikeSerializer

    def get_queryset(self):
         if self.request.user.role == 2:
             return Like.objects.filter(user=self.request.user)
         return Like.objects.all()



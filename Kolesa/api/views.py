from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, mixins
from api.service import CarFilter
# Create your views here.
from .models import City, Brand, Models, Comment
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from api.serializers import CitySerializer, BrandSerializer, CarSerializer, CarCreateSerializer, CommentSerializer


class CityAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        return CitySerializer

    def get_queryset(self):
        return City.objects.all()


class BrandAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        return BrandSerializer

    def get_queryset(self):
        return Brand.objects.all()

class CarAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class  = CarFilter
    print(CarFilter)
    print(filter_backends)

    def get_serializer_class(self):
        if(self.request.method == 'POST'):
            return CarCreateSerializer
        return CarSerializer
    def get_queryset(self):
        return Models.objects.all()




class CommentAPIView(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):


    permission_classes = (AllowAny,)

    serializer_class = CommentSerializer

    def get_queryset(self):
        print("Запрос 1")
        return Comment.objects.all()

    def perform_create(self, serializer):
        product = Models.objects.get(id=self.request.data.get('car'))
        serializer.save(user=self.request.user)
        serializer.save(product=product)
        serializer.save(value=self.request.data.get('value'))
        if (self.kwargs.get('parent') == None):
            pass
        else:
            parentComment = Comment.objects.get(id=self.request.data.get('parent'))
            if (parentComment.get('parent') == None):
                serializer.save(parent=parentComment)
            else:
                serializer.save(parent=parentComment.get('parent'))
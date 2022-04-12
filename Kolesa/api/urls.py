
from django.urls import path, include
from rest_framework import routers

from api.views import *

router = routers.DefaultRouter()
router.register(r'city', CityAPIViewset, basename='city')
router.register(r'brand', BrandAPIViewset, basename='brand')
router.register(r'model', CarAPIViewset, basename='model')
router.register(r'comment', CommentAPIView, basename='comment')

urlpatterns = [

]

urlpatterns += router.urls
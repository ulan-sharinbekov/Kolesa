from django.urls import path
from .views import UserCreateAPIView, UserUpdateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
urlpatterns = [
    path('signup/', UserCreateAPIView.as_view()),
    path('user/<int:pk>', UserUpdateAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify', TokenVerifyView.as_view()),
]
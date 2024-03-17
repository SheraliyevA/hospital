from django.urls import path
from django.contrib.auth import views as auth_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import *
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),


]
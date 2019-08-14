from django.urls import path

from .views import UserLoginAPIView, RegisterUsers

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
    path('users/register/', RegisterUsers.as_view(), name='register'),
]

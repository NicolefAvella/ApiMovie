from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import RegisterUsers, BlackList

app_name = 'user'
urlpatterns = [
    path('users/login/', obtain_jwt_token, name='login'),
    path('users/register/', RegisterUsers.as_view(), name='register'),
    path('users/logout/', BlackList.as_view(), name='logout'),
]

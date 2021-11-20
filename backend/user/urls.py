from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'user'

urlpatterns = [
    path('token/', obtain_auth_token, name='auth-token'),
    path('list/', views.UserList.as_view(), name='list'),
]

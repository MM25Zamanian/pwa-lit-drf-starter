from rest_framework import generics
from rest_framework import permissions
from . import models, serializer


class UserList(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserSerializer
    permission_classes = [permissions.IsAdminUser]

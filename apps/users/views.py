from rest_framework import generics
from apps.users.models import User
from apps.users.serializers import UserSerializer,UserCreateSerializer,UserUpdateSerializer

class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class UserUpdateAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer           
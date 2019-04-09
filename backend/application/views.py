from application.models import User
from rest_framework import generics
from application.serializer import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

from .models import User
from rest_framework.viewsets import ModelViewSet
from .serializer import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


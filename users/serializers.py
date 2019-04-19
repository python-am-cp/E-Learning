from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create(name=validated_data['name'],
                                   email=validated_data['email'],
                                   password=validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('name', 'email', 'password')

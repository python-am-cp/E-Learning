from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

#    def create(self, validated_data):
#        user = User(
#            email=validated_data['email'],
#            name=validated_data['username']
#        )
#        user.set_password(validated_data['password'])
#        user.save()
#        return user

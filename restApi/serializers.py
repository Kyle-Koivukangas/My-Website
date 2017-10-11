from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'isVerified', 'superuser')
        # to serialize/return all information:
        # fields = '__all__'


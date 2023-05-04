from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ("id", "first_name", "last_name", "email", "user_type", "password")

    def create(self, validated_data):
        user = User.objects.create(first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'],
                                        email=validated_data['email'],
                                        user_type=validated_data['user_type'],
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user
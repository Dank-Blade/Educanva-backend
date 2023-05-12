from rest_framework import serializers
from .models import User
from module.models import Module
from module.serializers import ModuleSerializer

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ("id", "first_name", "last_name", "email", "user_type", "password")
        read_only_fields = ("id",)  

    def create(self, validated_data):
        user = User.objects.create(first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'],
                                        email=validated_data['email'],
                                        user_type=validated_data['user_type'],
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ("id", "first_name", "last_name", "email", "user_type", "modules")
        read_only_fields = ("id",)  

    def create(self, validated_data):
        user = User.objects.create(first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'],
                                        email=validated_data['email'],
                                        user_type=validated_data['user_type'],
                                        modules=validated_data['modules'],
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class UserModuleSerializer(serializers.ModelSerializer): 
    modules = ModuleSerializer(many=True)

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "user_type", "modules")
        read_only_fields = ("id",)  

    def update(self, instance, validated_data):
        modules_data = validated_data.pop('modules', [])
        modules = []
        for module_data in modules_data:
            module, created = Module.objects.get_or_create(**module_data)
            modules.append(module)
        instance.modules.set(modules)
        return super().update(instance, validated_data)
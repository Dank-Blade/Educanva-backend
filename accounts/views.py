from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
# from rest_framework.response import Response
from rest_framework import generics
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# view for registering users
class RegisterView(generics.CreateAPIView):
    # def post(self, request):
    #     serializer = UserSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
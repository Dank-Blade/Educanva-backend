from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ModuleSerializer
from rest_framework import generics
from .models import Module

class CreateModule(generics.CreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class ModuleView(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    
class ModuleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
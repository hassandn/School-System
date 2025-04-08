from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.gis.geos import Point

class CustomUserCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    """
    API for create new user
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer



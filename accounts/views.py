from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserListSerializer, CustomUserDetailSerializer, CustomUserUpdateSerializer
from django.contrib.gis.geos import Point

class CustomUserCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    """
    API for create new user
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    """
    API for list all users
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserListSerializer


class CustomUserDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]  
    """
    API for retrieve user details
    """
    queryset = CustomUser.objects.all()  
    serializer_class = CustomUserDetailSerializer 

class CutomUserUpdateView(generics.UpdateAPIView):
    permission_classes = [AllowAny]  
    """
    API for update user information
    """
    queryset = CustomUser.objects.all()  
    serializer_class = CustomUserUpdateSerializer
    
 
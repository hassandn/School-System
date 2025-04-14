from rest_framework import generics
from rest_framework.permissions import AllowAny
from permissions import IsAdmin, IsTeacher, IsStudent, IsOwner
from .models import CustomUser
from .serializers import (
    CustomUserSerializer,
    CustomUserListSerializer,
    CustomUserDetailSerializer,
    CustomUserUpdateSerializer,
)
from django.contrib.gis.geos import Point
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

class CustomUserCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    """
    API for create new user
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserListView(generics.ListAPIView):
    permission_classes = [IsAdmin]
    """
    API for list all users
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserListSerializer


class CustomUserDetailView(generics.RetrieveAPIView):
    permission_classes = [IsOwner | IsAdmin]
    """
    API for retrieve user details
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailSerializer


class CutomUserUpdateView(generics.UpdateAPIView):
    permission_classes = [IsOwner | IsAdmin]
    """
    API for update user information
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserUpdateSerializer


class LogoutView(generics.GenericAPIView):
    """
    API for logging out a user.
    """
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **karargs):
        try:
            refresh_token = request.data.get('refresh_token')
            if not refresh_token:
                return Response({"detail": "No refresh token found."}, status=400)
            
                
            token = RefreshToken(refresh_token)
            
            token.blacklist()
            
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
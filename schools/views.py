from .serializers import SchoolSerializer
from .models import School
from rest_framework import generics
from rest_framework.permissions import AllowAny

class SchoolCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    """
    API for create new school
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


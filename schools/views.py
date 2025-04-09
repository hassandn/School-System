from .serializers import SchoolSerializer, CourseSerializer, ClassroomSerializer
from .models import School, Course, Classroom
from rest_framework import generics
from rest_framework.permissions import AllowAny

class SchoolCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    """
    API for create new school
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class CourseCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    """
    API for create new course
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ClassroomCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    """
    API for create new classroom
    """
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer    


class ClassroomUpdateView(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    """
    API for add student to classroom
    Teacher can add student to classroom
    """
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

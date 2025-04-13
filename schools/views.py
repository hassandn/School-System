from .serializers import (
    SchoolSerializer,
    CourseSerializer,
    ClassroomSerializer,
    ExerciseSerializer,
    NewSerializer,
    NearestSchoolsSerializer,
    AnswerSerializer,
    AddStudentToClassroomSerializer,
)
from permissions import IsOwner, IsTeacher, IsStudent, IsAdmin
from .models import School, Course, Classroom, Exercise, New, Answer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated


class SchoolCreateView(generics.CreateAPIView):
    permission_classes = [IsAdmin]
    """
    API for create new school
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class CourseCreateView(generics.CreateAPIView):
    permission_classes = [IsAdmin | IsTeacher]
    """
    API for create new course
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ClassroomCreateView(generics.CreateAPIView):
    permission_classes = [IsTeacher | IsAdmin]
    """
    API for create new classroom
    """
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class ClassroomUpdateView(generics.UpdateAPIView):
    permission_classes = [IsTeacher | IsAdmin]
    """
    API for add student to classroom
    Teacher can add student to classroom
    """
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class ExerciseCreateView(generics.CreateAPIView):
    permission_classes = [IsTeacher | IsAdmin]
    """
    API for create new exercise
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseUpdateView(generics.UpdateAPIView):
    permission_classes = [IsTeacher | IsAdmin]
    """
    API for update exercise
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class NewsCreateView(generics.CreateAPIView):
    permission_classes = [IsTeacher | IsAdmin]
    """
    API for create new news
    """
    queryset = New.objects.all()
    serializer_class = NewSerializer


class NewsUpdateView(generics.UpdateAPIView):
    permission_classes = [IsTeacher | IsAdmin]
    """
    API for update news
    """
    queryset = New.objects.all()
    serializer_class = NewSerializer


class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    """
    API for getting news details
    """
    queryset = New.objects.all()
    serializer_class = NewSerializer

    def get_object(self):
        obj = super().get_object()
        if self.request.user and self.request.user not in obj.viewed_by.all():
            obj.viewed_by.add(self.request.user)
            obj.save()
        return obj

    def get_queryset(self):
        return New.objects.all()


class NewsListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    """
    API for get all news
    """
    queryset = New.objects.all()
    serializer_class = NewSerializer


class NearestSchoolsListView(generics.ListAPIView):
    serializer_class = NearestSchoolsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.serializer_class.get_nearest_schools(self.request.user)


class SubmitAnswerView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]


class ListUserAnswersView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Answer.objects.filter(student=self.request.user)


class UpdateAnswerView(generics.UpdateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Answer.objects.filter(student=self.request.user)


class AddStudentToClassroomView(generics.UpdateAPIView):
    """
    API to add student to classroom by teacher using national code
    """

    queryset = Classroom.objects.all()
    serializer_class = AddStudentToClassroomSerializer
    permission_classes = [IsAuthenticated | IsTeacher ]

    def get_object(self):
        return Classroom.objects.get(id=self.kwargs["classroom_id"])

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["classroom"] = self.get_object()
        return context


class ReadMyClassrooms(generics.ListAPIView):
    """
    API to get all classrooms of student
    """
    serializer_class = ClassroomSerializer
    permission_classes = [IsStudent]

    def get_queryset(self):
        return Classroom.objects.filter(students=self.request.user)

from rest_framework import serializers
from django.contrib.gis.geos import Point
from .models import School, Course, Classroom, New, Exercise, Answer
from accounts.models import CustomUser

class SchoolSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(write_only=True)
    longitude = serializers.FloatField(write_only=True)
    
    teachers = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=CustomUser.objects.filter(role='teacher', registration_status='True')
    )

    class Meta:
        model = School
        fields = ["latitude", "longitude", "name", "description", "teachers"]

    def create(self, validated_data):
        latitude = validated_data.pop('latitude')
        longitude = validated_data.pop('longitude')
        teachers = validated_data.pop('teachers', [])
        # create a Point object using the latitude and longitude
        location = Point(longitude, latitude)
        school = School.objects.create(location=location, **validated_data)
        school.teachers.set(teachers)
        return school


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["name", "description", "schools"]


class ClassroomSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.filter(role='teacher', registration_status='True')
    )
    students = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=CustomUser.objects.filter(role='student', registration_status='True')
    )
    class Meta:
        model = Classroom
        fields = ["name", "course_name", "school", "teacher", "students", "teacher"]
        
    def creaet(self, validated_data):
        teacher = validated_data.pop('teachers', [])
        students = validated_data.pop('students', [])
        classroom = Classroom.objects.create(**validated_data)
        classroom.teachers.set(teacher)
        classroom.student.set(students)
        # classroom = Classroom.objects.create(**validated_data)
        return classroom


class ExerciseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Exercise
        fields = ["title", "description", "classroom", "author", "due_date"]


class NewSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.filter(role='teacher')
    )
    viewed_by = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=CustomUser.objects.all(),
        required=False
    )

    class Meta:
        model = New
        fields = ['id','title','content','school','classroom','author','viewed_by','date_created','date_updated',
        ]
        read_only_fields = ['date_created', 'date_updated']
        
        
        
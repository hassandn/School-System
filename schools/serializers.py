from rest_framework import serializers
from django.contrib.gis.geos import Point
from .models import School
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




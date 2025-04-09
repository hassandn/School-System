from rest_framework import serializers
from django.contrib.gis.geos import Point
from .models import School

class SchoolSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(write_only=True)
    longitude = serializers.FloatField(write_only=True)

    class Meta:
        model = School
        fields = "__all__"

    def create(self, validated_data):
        latitude = validated_data.pop('latitude')
        longitude = validated_data.pop('longitude')
        # create a Point object using the latitude and longitude
        location = Point(longitude, latitude)
        school = School.objects.create(location=location, **validated_data)
        return school




from rest_framework import serializers
from .models import CustomUser
from django.contrib.gis.geos import Point

class CustomUserSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(write_only=True)
    longitude = serializers.FloatField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'national_id', 'role', 'bio', 'latitude', 'longitude']


    def create(self, validated_data):
        latitude = validated_data.pop('latitude')
        longitude = validated_data.pop('longitude')
        # create a Point object using the latitude and longitude
        location = Point(longitude, latitude)
        user = CustomUser.objects.create(location=location, **validated_data)
        return user

    
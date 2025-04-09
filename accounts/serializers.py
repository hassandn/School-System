from rest_framework import serializers
from .models import CustomUser
from django.contrib.gis.geos import Point
from django.shortcuts import redirect
from django.urls import reverse

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


class CustomUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'national_id', 'role', 'bio', 'location', 'registration_status']


class CustomUserUpdateSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(write_only=True)
    longitude = serializers.FloatField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'bio', 'national_id', 'registration_status', 'latitude', 'longitude']

    def update(self, instance, validated_data):
        latitude = validated_data.pop('latitude', None)
        longitude = validated_data.pop('longitude', None)
        
        if latitude is not None and longitude is not None:
            location = Point(longitude, latitude)
            instance.location = location  

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()  
        return instance
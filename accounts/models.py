from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models as gis_models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    
    REGISTRATION_STATUS_CHOICES = (
        ('True', 'Registered'),
        ('pending', 'Pending'),
        ('False', 'Not Registered'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    national_id = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    location = gis_models.PointField(null=True, blank=True)  
    registration_status = models.CharField(max_length=7, choices=REGISTRATION_STATUS_CHOICES, default='pending')
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'national_id']
    
    def __str__(self):
        return self.username
    
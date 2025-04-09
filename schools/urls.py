from django.urls import path
from .views import SchoolCreateView

urlpatterns = [
    path('createschool/', SchoolCreateView.as_view(), name='create-school'),
]
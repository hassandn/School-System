from django.urls import path
from .views import SchoolCreateView, CourseCreateView, ClassroomCreateView

urlpatterns = [
    path('createschool/', SchoolCreateView.as_view(), name='create-school'),
    path('createcourse/', CourseCreateView.as_view(), name='create-course'),
    path('createclassroom/', ClassroomCreateView.as_view(), name='create-classroom'),
]
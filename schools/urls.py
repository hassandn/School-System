from django.urls import path,  include
from .views import SchoolCreateView, CourseCreateView, ClassroomCreateView, ClassroomUpdateView


urlpatterns = [
    path('createschool/', SchoolCreateView.as_view(), name='create-school'),
    path('createcourse/', CourseCreateView.as_view(), name='create-course'),
    path('createclassroom/', ClassroomCreateView.as_view(), name='create-classroom'),
    path('updateclassroom/<int:pk>/', ClassroomUpdateView.as_view(), name='update-classroom'),
    
]
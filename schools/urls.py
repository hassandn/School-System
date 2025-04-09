from django.urls import path,  include
from .views import SchoolCreateView, CourseCreateView, ClassroomCreateView, ClassroomUpdateView, ExerciseCreateView, ExerciseUpdateView, NewsCreateView, NewsUpdateView


urlpatterns = [
    path('createschool/', SchoolCreateView.as_view(), name='create-school'),
    path('createcourse/', CourseCreateView.as_view(), name='create-course'),
    path('createclassroom/', ClassroomCreateView.as_view(), name='create-classroom'),
    path('updateclassroom/<int:pk>/', ClassroomUpdateView.as_view(), name='update-classroom'),
    path('createexercise/', ExerciseCreateView.as_view(), name='create-exercise'),
    path('updateexercise/<int:pk>/', ExerciseUpdateView.as_view(), name='update-exercise'),
    path('createnews/', NewsCreateView.as_view(), name='create-news'),
    path('updatenews/<int:pk>/', NewsUpdateView.as_view(), name='update-news'),
]
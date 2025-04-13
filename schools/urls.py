from django.urls import path, include
from .views import (
    SchoolCreateView,
    CourseCreateView,
    ClassroomCreateView,
    ClassroomUpdateView,
    ExerciseCreateView,
    ExerciseUpdateView,
    NewsCreateView,
    NewsUpdateView,
    NewsDetailView,
    NewsListView,
    NearestSchoolsListView,
    SubmitAnswerView,
    ListUserAnswersView,
    UpdateAnswerView,
)


urlpatterns = [
    path("createschool/", SchoolCreateView.as_view(), name="create-school"),
    path("createcourse/", CourseCreateView.as_view(), name="create-course"),
    path("createclassroom/", ClassroomCreateView.as_view(), name="create-classroom"),
    path("updateclassroom/<int:pk>/",ClassroomUpdateView.as_view(),name="update-classroom",),
    path("createexercise/", ExerciseCreateView.as_view(), name="create-exercise"),
    path("updateexercise/<int:pk>/", ExerciseUpdateView.as_view(), name="update-exercise"),
    path("createnews/", NewsCreateView.as_view(), name="create-news"),
    path("updatenews/<int:pk>/", NewsUpdateView.as_view(), name="update-news"),
    path("new/<int:pk>/", NewsDetailView.as_view(), name="news-detail"),
    path("news/", NewsListView.as_view(), name="news-list"),
    path("nearestschools/", NearestSchoolsListView.as_view(), name="nearest-schools"),
    path("exercise/submitanswer/", SubmitAnswerView.as_view(), name="submit-answer"),
    path('exercise/myanswers/', ListUserAnswersView.as_view(), name='list-my-answers'),
    path('exercise/updateanswer/<int:pk>/', UpdateAnswerView.as_view(), name='update-answer'),
]

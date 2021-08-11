from django.urls import path

from exercises.api.v1.views import ExerciseListAPIView, PlayerListAPIView

urlpatterns = [
    path("", ExerciseListAPIView.as_view(), name="exercise_list"),
    path("players", PlayerListAPIView.as_view(), name="player_list"),
]
from rest_framework.generics import ListAPIView

from exercises.api.v1.serializers import ExerciseSerializer, PlayerSerializer
from exercises.models import Exercise, Player


class ExerciseListAPIView(ListAPIView):
    """Exercise List API View."""

    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()


class PlayerListAPIView(ListAPIView):
    """Player List API View."""

    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

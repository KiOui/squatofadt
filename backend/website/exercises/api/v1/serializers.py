from rest_framework import serializers

from exercises.models import Exercise, Player


class ExerciseSerializer(serializers.ModelSerializer):
    """Exercises Serializer."""

    class Meta:
        """Meta class."""

        model = Exercise
        fields = ["name", "min_range_amount", "max_range_amount"]


class PlayerSerializer(serializers.ModelSerializer):
    """Player Serializer."""

    class Meta:
        """Meta class."""

        model = Player
        fields = ["name", "multiplier"]

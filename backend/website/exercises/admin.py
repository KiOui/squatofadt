from django.contrib import admin
from django.contrib.admin import ModelAdmin

from exercises import models


@admin.register(models.Exercise)
class ExerciseAdmin(ModelAdmin):
    """Exercise Admin."""

    pass


@admin.register(models.Player)
class PlayerAdmin(ModelAdmin):
    """Player Admin."""

    pass

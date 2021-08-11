from django.db import models


class Exercise(models.Model):
    """Exercise model."""

    name = models.CharField(max_length=1024, help_text="Name of the exercise", blank=False, null=False)
    min_range_amount = models.IntegerField(default=2, help_text="Minimum of the range where a random amount for this "
                                                                "exercise will be picked out of", blank=False,
                                           null=False)
    max_range_amount = models.IntegerField(default=5, help_text="Maximum of the range where a random amount for this "
                                                                "exercise will be picked out of", blank=False,
                                           null=False)

    def save(self, *args, **kwargs):
        """Save."""
        if self.min_range_amount > self.max_range_amount:
            raise ValueError("Minimum range should be smaller or equal than maximum range")

        if self.min_range_amount < 1:
            raise ValueError("Minimum range should be bigger than 1")

        if self.max_range_amount < 1:
            raise ValueError("Maximum range should be bigger than 1")

        return super(Exercise, self).save(*args, **kwargs)

    def __str__(self):
        """Convert this object to string."""
        return self.name


class Player(models.Model):
    """Player model."""

    name = models.CharField(max_length=1024, help_text="Name of the player", blank=False, null=False)
    multiplier = models.IntegerField(default=1, help_text="How many chances per roll a player gets for losing", blank=False, null=False)

    def save(self, *args, **kwargs):
        """Save."""
        if self.multiplier < 1:
            raise ValueError("Multiplier should be bigger than 1")

        return super(Player, self).save(*args, **kwargs)

    def __str__(self):
        """Convert this object to string."""
        return self.name

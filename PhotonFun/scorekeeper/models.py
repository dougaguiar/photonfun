from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Match(models.Model):
    referee = models.ForeignKey(User, related_name="referee", on_delete=models.DO_NOTHING)
    match_datetime = models.DateTimeField(default=timezone.now)
    player_a = models.ForeignKey(User, related_name="first_player", on_delete=models.DO_NOTHING)
    player_b = models.ForeignKey(User, related_name="second_player", on_delete=models.DO_NOTHING)
    points_a = models.IntegerField(blank=True, null=True)
    points_b = models.IntegerField(blank=True, null=True)

    OUTCOMES = (
        ('W', 'Win'),
        ('L', 'Lose'),
    )
    outcome_a = models.CharField(max_length=2, choices=OUTCOMES)
    outcome_b = models.CharField(max_length=2, choices=OUTCOMES)

    class Meta:
        ordering = ['match_datetime']

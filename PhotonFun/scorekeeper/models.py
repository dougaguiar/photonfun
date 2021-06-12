from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


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

    player_a_increment = models.FloatField(default=0,blank=True)
    player_b_increment = models.FloatField(default=0,blank=True)

    class Meta:
        ordering = ['match_datetime']

    def get_absolute_url(self):
        return reverse('match-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Match {self.id}'

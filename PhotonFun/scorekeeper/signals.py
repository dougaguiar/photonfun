from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Match
from decimal import *


# In Pre save, calculates increments for the match
@receiver(pre_save, sender=Match)
def calculate_ranking_change(sender, instance, **kwargs):
    k_factor = 40
    rank_a = float(instance.player_a.profile.single_points)
    rank_b = float(instance.player_b.profile.single_points)
    points_a = instance.points_a
    points_b = instance.points_b
    player_a_increment = k_factor * (points_a / (points_a + points_b) - rank_a / (rank_a + rank_b))
    player_b_increment = k_factor * (points_b / (points_a + points_b) - rank_b / (rank_a + rank_b))
    instance.player_a_increment = Decimal(player_a_increment)
    instance.player_b_increment = Decimal(player_b_increment)
    if points_a > points_b:
        instance.outcome_a = 'W'
        instance.outcome_b = 'L'
    else:
        instance.outcome_b = 'W'
        instance.outcome_a = 'L'


# In post save, applies ranking changes to players and updates everyone's ranking
@receiver(post_save, sender=Match)
def update_player_points(sender, instance, created, **kwargs):
    # Get players from match and update their points
    instance.player_a.profile.single_points += instance.player_a_increment
    instance.player_a.profile.save()

    instance.player_b.profile.single_points += instance.player_b_increment
    instance.player_b.profile.save()


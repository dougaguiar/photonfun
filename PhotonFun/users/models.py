from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    single_points = models.DecimalField(default=500, max_digits=6, decimal_places=2)
    double_points = models.DecimalField(default=500, max_digits=6, decimal_places=2)
    single_ranking = models.IntegerField(default=0)
    double_ranking = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'

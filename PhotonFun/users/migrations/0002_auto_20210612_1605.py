# Generated by Django 3.2.4 on 2021-06-12 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='points',
            new_name='single_points',
        ),
        migrations.AddField(
            model_name='profile',
            name='doubles_points',
            field=models.FloatField(default=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='doubles_ranking',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='singles_ranking',
            field=models.IntegerField(default=0),
        ),
    ]

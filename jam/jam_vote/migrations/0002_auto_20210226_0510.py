# Generated by Django 3.1.5 on 2021-02-26 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jam_vote', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BestTeam',
        ),
        migrations.DeleteModel(
            name='FavoriteTeam',
        ),
        migrations.DeleteModel(
            name='YourTeam',
        ),
        migrations.AddField(
            model_name='team',
            name='bestTeamCount',
            field=models.IntegerField(default=0, verbose_name='トリがいいと言われた数'),
        ),
        migrations.AddField(
            model_name='team',
            name='favoriteTeamCount',
            field=models.IntegerField(default=0, verbose_name='気に入られた数'),
        ),
        migrations.AddField(
            model_name='team',
            name='yourTeamCount',
            field=models.IntegerField(default=0, verbose_name='チームのメンバー数'),
        ),
    ]

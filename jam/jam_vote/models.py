from django.db import models

class Question(models.Model):
    title = models.CharField('タイトル', max_length=100)

    def __str__(self):
        return self.title

class Team(models.Model):
    teamname = models.CharField('チーム名', max_length=30)
    yourTeamCount = models.IntegerField('チームのメンバー数', default=0, blank=True, null=True)
    favoriteTeamCount = models.IntegerField('気に入られた数', default=0, blank=True, null=True)
    bestTeamCount = models.IntegerField('トリがいいと言われた数', default=0, blank=True, null=True)
    title = models.ForeignKey(Question, verbose_name='タイトル',
        blank=False, null=False,
        on_delete=models.CASCADE)
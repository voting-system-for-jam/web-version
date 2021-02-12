from django.db import models



# class Post(models.Model):
#     author = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
#     title = models.CharField('タイトル', max_length=50)
#     content = models.TextField('内容', max_length=1000)
#     category = models.ForeignKey('Category', on_delete=models.PROTECT)
#     thumbnail = models.ImageField(upload_to="images/", blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title


class Question(models.Model):
    title = models.CharField('タイトル', max_length=100)


class Team(models.Model):
    teamname = models.CharField('チーム名', max_length=30)

class YourTeam(models.Model):
    teamname = models.CharField('チーム名', max_length=30)
    result = models.IntegerField('結果', default=0)

class FavoriteTeam(models.Model):
    teamname = models.CharField('チーム名', max_length=30)
    result = models.IntegerField('結果', default=0)

class BestTeam(models.Model):
    teamname = models.CharField('チーム名', max_length=30)
    result = models.IntegerField('結果', default=0)


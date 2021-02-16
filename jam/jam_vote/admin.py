from django.contrib import admin
from .models import Question, Team

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # カンマをつけることで、リストと認識させる
    list_display = ('title',)
    list_display_links = ('title',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    # カンマをつけることで、リストと認識させる
    list_display = ('teamname','title')
    list_display_links = ('teamname',)

from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # カンマをつけることで、リストと認識させる
    list_display = ('title',)
    list_display_links = ('title',)
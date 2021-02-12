from django.urls import path
from . import views

app_name = 'jam_vote'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('make', views.MakeView.as_view(), name='make'),
    path('answer',views.AnswerView.as_view(),name='answer')
]
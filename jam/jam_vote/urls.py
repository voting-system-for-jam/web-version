from django.urls import path
from . import views

app_name = 'jam_vote'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('make', views.add, name='make'),
    path('answer/<int:pk>', views.AnswerView.as_view(), name='answer'),
    path('result/<int:pk>', views.ResultsView.as_view(), name='result'),
    path('answer_end',views.AnswerEndView.as_view() ,name='answer_end'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]
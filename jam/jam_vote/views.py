from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

from .models import Question
from .forms import VoteForm

# Create your views here.

class Index(TemplateView):
    template_name = 'jam_vote/index.html'

    # model(データベース)から色々引っ張ってくる
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     post_list = Post.objects.all().order_by('-created_at')
    #     context = {
    #         'post_list': post_list,
    #     }
    #     return context


class MakeView(CreateView):
    template_name = 'jam_vote/make.html'
    model = Question
    form_class = VoteForm
    success_url = reverse_lazy('jam_vote:index')

class AnswerView(TemplateView):
    template_name = 'jam_vote/answer.html'
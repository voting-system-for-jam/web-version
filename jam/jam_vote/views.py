from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView

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
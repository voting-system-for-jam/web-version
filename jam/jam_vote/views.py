from django.shortcuts import render,redirect
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

from .models import Question, Team
from .forms import QuestionForm, TeamForm, PostCreateFormSet

# Create your views here.

class Index(TemplateView):
    template_name = 'jam_vote/index.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        question_list = Question.objects.all().order_by('id')
        context = {
            'question_list':question_list,
        }
        return context
    # model(データベース)から色々引っ張ってくる
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     post_list = Post.objects.all().order_by('-created_at')
    #     context = {
    #         'post_list': post_list,
    #     }
    #     return context


# class MakeView(CreateView):
#     template_name = 'jam_vote/make.html'
#     model = Question
#     form_class = VoteForm
#     success_url = reverse_lazy('jam_vote:index')

def add(request):
    question = QuestionForm(request.POST or None)
    context = {'question': question}
    if request.method == 'POST' and question.is_valid():
        post = question.save(commit=False)
        formset = PostCreateFormSet(request.POST, instance=post)  # 今回はファイルなのでrequest.FILESが必要
        if formset.is_valid():
            post.save()
            formset.save()
            return redirect('jam_vote:index')

        # エラーメッセージつきのformsetをテンプレートへ渡すため、contextに格納
        else:
            context['formset'] = formset

    # GETのとき
    else:
        # 空のformsetをテンプレートへ渡す
        context['formset'] = PostCreateFormSet()


    return render(request, 'jam_vote/make.html', context)


class AnswerView(DetailView):
    model = Question
    template_name = 'jam_vote/answer.html'

    def get_context_data(self, *args, **kwargs):
        detail_data = Question.objects.get(id=self.kwargs['pk'])
        team_list = Team.objects.filter(title_id=self.kwargs['pk'])
        context = {
            'object': detail_data,
            'team_list': team_list,
        }
        return context

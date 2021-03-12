from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

from .models import Question, Team
from .forms import QuestionForm, TeamForm, PostCreateFormSet
from django.http.response import HttpResponseRedirect,HttpResponse
from django.urls.base import reverse

import io
# matplotlibをimport
import matplotlib.pyplot as plt

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


def add(request):
    question = QuestionForm(request.POST or None)
    context = {'question': question}
    if request.method == 'POST' and question.is_valid():
        post = question.save(commit=False)
        formset = PostCreateFormSet(request.POST, instance=post) 
        print(formset)
        if formset.is_valid():
            post.save()
            formset.save()
            return redirect('jam_vote:index')

        else:
            print("OK")
            context['formset'] = formset

    else:
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


class AnswerEndView(TemplateView):
    template_name = 'jam_vote/answer_end.html'


class ResultsView(DetailView):
    model = Question
    template_name = 'jam_vote/result.html'

#png画像形式に変換数関数
def plt2png():
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=200)
    s = buf.getvalue()
    buf.close()
    return s

#画像埋め込み用view
def img_plot(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    detail_data = Question.objects.get(id=question_id)
    team_list = Team.objects.filter(title_id=question_id)
    x = []
    y = []
    p = []
    q = []
    try:
        for team in question.team_set.all():
            x.append(team.teamname)
            y.append(team.favoriteTeamCount)
        for team in question.team_set.all():
            p.append(team.teamname)
            q.append(team.bestTeamCount)
    except (KeyError, Team.DoesNotExist):
        return render(request, 'jam_vote/index.html', {
            'question': question,
            'error_message': "選択していない選択肢があります",
        })

    # matplotを使って作図する
    fig, ax = plt.subplots(nrows=1, ncols=2)
    fig.autofmt_xdate(rotation=45)
    ax[0].set_title('FavoriteTeam')
    ax[1].set_title('BestTeam')
    ax[0].bar(x, y)
    ax[1].bar(p, q)
    png = plt2png()
    plt.cla()
    response = HttpResponse(png, content_type='image/png')
    return response

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        your_team_choice = question.team_set.get(pk=request.POST['your_team'])
        favorite_team_choice = question.team_set.get(pk=request.POST['favorite_team'])
        best_team_choice = question.team_set.get(pk=request.POST['best_team'])

    except (KeyError, Team.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'jam_vote/index.html', {
            'question': question,
            'error_message': "選択していない選択肢があります",
        })
    else:
        your_team_choice.yourTeamCount += 1
        your_team_choice.save(update_fields=['yourTeamCount'])
        favorite_team_choice.favoriteTeamCount += 1
        favorite_team_choice.save(update_fields=['favoriteTeamCount'])
        best_team_choice.bestTeamCount += 1
        best_team_choice.save(update_fields=['bestTeamCount'])
        return HttpResponseRedirect(reverse('jam_vote:answer_end'))

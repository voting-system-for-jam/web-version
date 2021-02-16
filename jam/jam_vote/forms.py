from django import forms

from .models import Question, Team

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title',)

    # 見た目を整えるのに使います
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('teamname',)

    # 見た目を整えるのに使います
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


PostCreateFormSet = forms.inlineformset_factory(
    Question, Team, fields='__all__', form=TeamForm, extra=1, can_delete=True
)
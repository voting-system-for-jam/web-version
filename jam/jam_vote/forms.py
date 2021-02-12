from django import forms

from .models import Question

class VoteForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title',)

    # 見た目を整えるのに使います
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
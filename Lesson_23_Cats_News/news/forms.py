from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['nick_name', 'content', 'parent_comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent_comment'].widget = forms.HiddenInput()

    def set_parent_comment_choices(self, parent_comment_choices):
        self.fields['parent_comment'].queryset = parent_comment_choices

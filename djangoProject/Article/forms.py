from django import forms
from Article.models import ArticlePost

class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ['title', 'content', 'column', 'tags', 'avatar']






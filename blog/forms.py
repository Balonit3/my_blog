from django import forms
from .models import Post,Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Указываем модель
        fields = ['title', 'content', 'category']

        labels = {
            'title': 'Заголовок',
            'content': 'Текст поста',
            'category': 'Категория'
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5})}
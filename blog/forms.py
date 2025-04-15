from django import forms
from .models import Post,Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','category']
        widgets = {
            'category':forms.Select(attrs={'class':'form-control'})
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['category'].queriset=Category.objects.all()
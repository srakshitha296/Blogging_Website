from django import forms
from .models import Post

class blogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','author','content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


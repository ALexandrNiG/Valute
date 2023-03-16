from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    name = forms.CharField(label='Название поста',
                           widget=forms.TextInput(attrs={'placeholder': "Название", 'class': 'form-control'}))
    text = forms.CharField(label='Текст поста',
                           widget=forms.Textarea(attrs={'placeholder': "Текст поста", 'class': 'form-control'}))

    class Meta:
        model = Post
        fields = '__all__'
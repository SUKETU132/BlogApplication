from django import forms
from .models import Blog_app

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog_app
        fields = ['title', 'description', 'blog_image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }


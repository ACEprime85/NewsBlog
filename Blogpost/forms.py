from django import forms
from .models import Blogpost, Video, Comment

class BlogpostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = [
            'title',
            'slug',
            'body',
            'tags',
]


class VideoForm(forms.ModelForm):
    class Meta:
        model= Video
        fields= ["name", "videofile"]


class CommentForm(forms.ModelForm):    
    class Meta:        
        model = Comment        
        fields = ('name', 'email', 'body')


class contactForm(forms.Form):
    name =forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget = forms.Textarea)
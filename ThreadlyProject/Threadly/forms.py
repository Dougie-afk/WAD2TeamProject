from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Post, Comments


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=32, help_text="Enter your username.")
    profile_picture = forms.ImageField(required=False, help_text="Upload your profile picture.")
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, help_text="Enter a strong password.")
    class Meta:
        model = User
        fields = ('username', 'profile_picture', 'password')

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea, max_length=1000,help_text="Enter the post content.")
    image = forms.ImageField(required=False, help_text="Upload image (optional)")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)  

    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'threadID')#

class CommentForm(forms.ModelForm):
    content = forms.CharField(help_text="Enter your comment.")

    class Meta:
        model = Comments
        fields = ('postID', 'content')




from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Post, Comments

# User Registration Form
class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=32, help_text="Enter your username.")
    profile_picture = forms.URLField(required=False, help_text="Enter your profile picture URL.")
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, help_text="Enter a strong password.")
    class Meta:
        model = User
        fields = ('username', 'profile_picture', 'password')


# Post Form
class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text="Enter the post title.")
    content = forms.CharField(widget=forms.Textarea, help_text="Enter the post content.")
    image = forms.URLField(required=False, help_text="Enter an image URL for the post.")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)  # Hidden field

    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'thread')


# Comment Form
class CommentForm(forms.ModelForm):
    content = forms.CharField(help_text="Enter your comment.")

    class Meta:
        model = Comments
        fields = ('post', 'content')




from django import forms
from django.db.models import fields

from .models import Comment  # form for users to comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,      widget=forms.Textarea)


# ModelForm is used because we want to use the form dynamically.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


# This is for the full text serach feature
class SearchForm(forms.Form):
    query = forms.CharField()

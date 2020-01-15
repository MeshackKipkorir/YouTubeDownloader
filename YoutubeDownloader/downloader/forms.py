from django import forms

class YouTubeLinks(forms.Form):
    link = forms.CharField(max_length=100)
    
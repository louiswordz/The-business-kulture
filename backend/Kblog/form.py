from django import forms

class searchform(forms.Form):
    text = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':'search-bar',
        'placeholder':'Search news'
        }))
    
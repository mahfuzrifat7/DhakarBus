from django import forms

class SearchForm(forms.Form):
    source = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Source'}))
    destination = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Destination'}))
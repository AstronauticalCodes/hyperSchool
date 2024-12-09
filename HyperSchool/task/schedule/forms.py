from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label="Search for Courses", max_length=100)
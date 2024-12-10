from django import forms
from .models import Student

class SearchForm(forms.Form):
    query = forms.CharField(label="Search for Courses", max_length=100)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'age', 'course']
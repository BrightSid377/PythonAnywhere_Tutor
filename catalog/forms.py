


# forms.py

from django import forms
from .models import Student, Tutor

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'

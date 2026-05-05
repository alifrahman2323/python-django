from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = ['title', 'description', 'created_at']

        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'})
        }
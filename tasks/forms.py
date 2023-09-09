from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['Title', 'Description', 'Finished_at', 'Completed']

    Finished_at = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    STATUS_CHOICES = [
        ('', 'All'),
        ('1', 'Completed'),
        ('0', 'Not Completed'),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False)

    SORT_CHOICES = [
        ('Created_at', 'Created At (Increasing)'),
        ('-Created_at', 'Created At (Decreasing)'),
    ]
    sort = forms.ChoiceField(choices=SORT_CHOICES, required=False)
class DeleteTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = []

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['Title', 'Description', 'Finished_at', 'Completed']


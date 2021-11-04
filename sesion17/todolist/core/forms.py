from django import forms
 
from core.models import Task

class TaskForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget= forms.Textarea)

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'due_date')
from django import forms
from .models import PhotoReport

class PhotoReportForm(forms.ModelForm):
    class Meta:
        model = PhotoReport
        fields = ['title', 'location','photo', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input'}),
            'location': forms.TextInput(attrs={'class': 'input'}),
            'photo': forms.FileInput(attrs={'class': 'input'}),
            'description': forms.Textarea(attrs={'class': ''}),
        }

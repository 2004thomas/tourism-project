from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['place', 'content', 'image']
        widgets = {
            'place': forms.Select(attrs={'class':'form-select'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
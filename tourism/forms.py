from django import forms
from .models import Review,Photo

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['place', 'review_text']
#         widgets = {
#             'place': forms.Select(attrs={'class':'form-select'}),
#             'review_text': forms.Textarea(attrs={'class':'form-control'}),
            
#         }

# 'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),





class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['place', 'review_text', 'rating']

        widgets = {
            'place': forms.Select(attrs={'class': 'form-select'}),
            'review_text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'maxlength': 150,
                'placeholder': 'Write your experience (max 150 words)'
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 5
            })
        }


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['place', 'image']

        widgets = {
            'place': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }
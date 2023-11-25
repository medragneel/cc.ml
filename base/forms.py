# forms.py
from django import forms
from .models import UploadImage


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = ['image']
        # widgets = {
        #     'image': forms.ClearableFileInput(attrs={'class': 'p-2'}),
        # }

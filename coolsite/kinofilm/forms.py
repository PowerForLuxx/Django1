from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Movie
        fields = ['Name', 'Description', 'photo', 'cat']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        Name = self.cleaned_data['Name']
        if len(Name) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return Name

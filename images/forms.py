from .models import Image
from django import forms


class UserImageForm(forms.ModelForm):
    class Meta:
        # To specify the model to be used to create form
        model = Image
        # Includes all the fields of model
        exclude = ['author', 'height', 'width']

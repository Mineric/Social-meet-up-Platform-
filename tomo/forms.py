from django import forms
from .models import *

class UploadEventImageForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['cover_image']

class UploadUserAvatarImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar_image']
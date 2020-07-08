from django import forms
from . models import AppModel

class AppsForm(forms.ModelForm):
    
    class Meta:
        model = AppModel
        fields = [
            "title",
            "desc",
        ]
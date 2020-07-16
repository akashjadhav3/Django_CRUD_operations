from django import forms
from . models import AppModel

class AppsForm(forms.ModelForm):
    
    class Meta:
        model = AppModel
        fields = [
            "title",
            "desc",
        ]

    def cleaned_title(self, *args, **kwargs):
        title = self.cleaned_data.get["title"]
        qs = AppModel.objects.filter(title__iexact=title)
        if qs.exists():
            raise forms.ValidationError("This title is already in use")
        return title
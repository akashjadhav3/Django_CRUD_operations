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
        instance = self.instance
        title = self.cleaned_data.get["title"]
        qs = AppModel.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This title is already in use")
        return title
from django.shortcuts import render
from .models import AppModel
from .forms import AppsForm

def create_view(request):
    context = {}

    form = AppsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form']= form
    return render(request,"create_view.html", context)

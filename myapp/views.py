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

def list_view(request):
    context = {}
    context["dataset"]=AppModel.objects.all()   

    return render(request,'list_view.html',context)

def detail_view(request,id):
    context = {}

    context["data"]= AppModel.objects.get(id=id)

    return render(request,'detail_view.html',context)



from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect,redirect)
from .models import AppModel
from .forms import AppsForm


# @login_required   # two way to do this
@staff_member_required
def create_view(request):
    context = {}
    form = AppsForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        # obj = AppModel.objects.create(**form.cleaned_data) # also used to create when form.Form in form.py
        obj.save()
    context['form']= form
    return render(request,"create_view.html", context)

def list_view(request):
    context = {}
    context["dataset"]=AppModel.objects.all()
    # context["dataset"]=AppModel.objects.filter(title__icontains='hello') #search hello title list
    return render(request,'list_view.html',context)

def detail_view(request,id):
    context = {}
    # context["data"]= AppModel.objects.get(id=id)
    context["data"]= get_object_or_404(AppModel,id=id)
    return render(request,'detail_view.html',context)

def update_view(request,id):
    context = {}
    obj = get_object_or_404(AppModel,id=id)
    form = AppsForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/list")
    context["form"]=form
    return render(request,'update_view.html',context)

def delete_view(request,id):
    context={}
    obj = get_object_or_404(AppModel,id=id)
    if request.method =='POST':
        obj.delete()
        # return HttpResponseRedirect('/list')
        return redirect('/list')
    return render(request,'delete_view.html',context)




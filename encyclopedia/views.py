from django.shortcuts import render, redirect

from . import util
from .models import baikemodel
from .forms import baikeform
from django.urls import reverse
from django.http import HttpResponse

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def baike_add(request):
    if request.method == 'POST':
        form = baikeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse(list))
    else:
        form = baikeform()
    return render(request,'entry.html',{"form":form})

def baike_list(request):
    baikes=baikemodel.objects.all()
    return render(request,'list.html',{'baikes':baikes})
    



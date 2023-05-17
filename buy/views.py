from django.http import HttpResponse
from django.shortcuts import render
from buy import models
# Create your views here.

def hello_world(request):
    return render(request,'first.html',{})

def runoob(request):
    name = request.POST.get("name")
    return HttpResponse('姓名：{}'.format(name))


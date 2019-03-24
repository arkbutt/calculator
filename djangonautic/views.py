from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    # return HttpResponse('about1111')
    return render(request,"about.html")

def homepage(request):
    # return HttpResponse('homepage')
    return render(request,"homepage.html")
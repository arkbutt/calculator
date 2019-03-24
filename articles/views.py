from django.shortcuts import render

from django.http import HttpResponse

def article_list(request):
    return render(request,'articles/article_list.html')

def index(request):
    a = int(request.GET['A'])
    Op= request.GET['Op']
    b = int(request.GET['B'])
    z=""
    if Op == '+':
        z = a + b
    elif Op == '-':
        z = a - b
    elif Op == '*':
        z = a * b
    elif Op == '/':
        z = a / b
    else:
        z = "invalid Mathamatical Operator"

    return HttpResponse("<h1>Hello, world. %s</h1>" %(z))

from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {} )

def indexpage(request):
    return render(request, 'base.html', {} )    
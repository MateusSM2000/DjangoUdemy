from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_view(request):
    return HttpResponse('blog view app 1')

def articles_view(request):
    return HttpResponse('blog/articles view')
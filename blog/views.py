from django.shortcuts import render


# Create your views here.

def my_view(request):
    return render(request, 'blog/index.html')

def articles_view(request):
    return render(request, 'blog/articles.html')
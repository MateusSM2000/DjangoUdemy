from django.shortcuts import render
import requests


# Create your views here.

def my_view(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
    else:
        posts = [{'Erro ao buscar os dados': response.status_code}]

    context = {
        'title': '- Blog',
        'posts': posts,
    }

    return render(request, 'blog/index.html', context)

def articles_view(request):
    context = {
        'text': 'BLOG/ARTICLES',
        'title': '- Articles',
    }

    return render(request, 'blog/articles.html', context)
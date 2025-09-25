from django.shortcuts import render


# Create your views here.

def my_view(request):
    context = {
        'text': 'BLOG',
        'title': '- Blog',
    }

    return render(request, 'blog/index.html', context)

def articles_view(request):
    context = {
        'text': 'BLOG/ARTICLES',
        'title': '- Articles',
    }

    return render(request, 'blog/articles.html', context)
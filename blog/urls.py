
from django.urls import path
from blog import views as blog_views

app_name = 'blog'

urlpatterns = [
    path('', blog_views.my_view, name='index'),
    path('articles/', blog_views.articles_view, name='articles'),
]

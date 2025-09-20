
from django.urls import path
from blog import views as blog_views



urlpatterns = [
    path('', blog_views.my_view),
    path('articles/', blog_views.articles_view),
]

from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMs',
        'title': 'blog post one',
        'content': 'first post content',
        'date_posted': 'january 16, 2020'
    },
    {
        'author': 'Przemsaj',
        'title': 'blog post two',
        'content': 'second post content',
        'date_posted': 'january 16, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

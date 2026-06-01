from django.shortcuts import render
from django.http import HttpResponse


# dummy data
posts = [
    {
        'author':'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author':'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 28, 2018'
    },
    {
        'author':'Mike Koe',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'June 08, 2025'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')

    return render(request, 'blog/about.html', {'title':'about'})



# blog -> templates -> blog  templates.html is live


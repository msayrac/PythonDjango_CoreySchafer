from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html', context)

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')

    return render(request, 'blog/about.html', {'title':'about'})



# blog -> templates -> blog  templates.html is live


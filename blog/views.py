from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView
)
from django.http import HttpResponse
from .models import Post

# Create your views here.
# class based view
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # default olarak blog/post_list.html altında arıyor. Biz route bu seklilde manuel olarak verdik
    context_object_name = 'posts'
    ordering = ['-date_posted']

# function based view
def home(request):    
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html', context)


# class based view
class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html', {'title':'about'})


# blog -> templates -> blog  templates.html is live


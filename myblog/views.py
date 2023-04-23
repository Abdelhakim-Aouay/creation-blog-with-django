from django.shortcuts import render
from.models import Post
from django.views.generic import ListView, DeleteView, DetailView
# Create your views here.
def home(request):
    return render(request, 'myblog/home.html', {})

class HomeListView(ListView):
    model=Post
    template_name="myblog/home.html"
    
    
class ArticleDetailView(DetailView):
    model=Post
    template_name="myblog/article.html"
    

from django.shortcuts import render
from.models import Post
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from.forms import AddForm



class HomeListView(ListView):
    model=Post
    template_name="myblog/home.html"
    ordering=['-id']
    
    
class ArticleDetailView(DetailView):
    model=Post
    template_name="myblog/article.html"
    
class AddPostView(CreateView):
    model=Post
    template_name="myblog/add.html"
    form_class=AddForm
from django.urls import reverse_lazy


class UpdatePostView(UpdateView):
    model=Post
    template_name="myblog/modifier.html"
    form_class=AddForm
    success_url= reverse_lazy('home')
    
class DeletePostView(DeleteView):
    model=Post
    template_name="myblog/supp.html"
    success_url= reverse_lazy('home')
    
    

from django.shortcuts import render
from.models import Post, Category
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from.forms import AddForm
from django.urls import reverse_lazy



class HomeListView(ListView):
    model=Post
    template_name="myblog/home.html"
    ordering=['-created_at']
    #ordering=['-id']
    
    
class ArticleDetailView(DetailView):
    model=Post
    template_name="myblog/article.html"
    
class AddPostView(CreateView):
    model=Post
    template_name="myblog/add.html"
    form_class=AddForm
    
class AddCategoryView(CreateView):
    model=Category
    template_name="myblog/category.html"
    fields ="__all__"
    
def categoryView(request, cat):
    category_post=Post.objects.filter(category=cat)
    return render(request, 'myblog/categories.html', {'cat':cat.title(), 'category_post': category_post})

print(Post.objects.filter(category="encoding"))
    
    



class UpdatePostView(UpdateView):
    model=Post
    template_name="myblog/modifier.html"
    form_class=AddForm
    success_url= reverse_lazy('home')
    
class DeletePostView(DeleteView):
    model=Post
    template_name="myblog/supp.html"
    success_url= reverse_lazy('home')
    
    

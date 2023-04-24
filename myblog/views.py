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
    
    def get_context_data(self,**kwargs): 
        cat_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context
    
class ArticleDetailView(DetailView):
    model=Post
    template_name="myblog/article.html"
    def get_context_data(self,**kwargs): 
        cat_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context
    
class AddPostView(CreateView):
    model=Post
    template_name="myblog/add.html"
    form_class=AddForm
    def get_context_data(self,**kwargs): 
        cat_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context
    
class AddCategoryView(CreateView):
    model=Category
    template_name="myblog/category.html"
    fields ="__all__"
    def get_context_data(self,**kwargs): 
        cat_menu = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context
def categoryView(request, cat):
    category_post=Post.objects.filter(category=cat.replace('-', ' '))
    return render(request, 'myblog/categories.html', {'cat':cat.title().replace('-', ' '), 'category_post': category_post})




    



class UpdatePostView(UpdateView):
    model=Post
    template_name="myblog/modifier.html"
    form_class=AddForm
    success_url= reverse_lazy('home')
    
class DeletePostView(DeleteView):
    model=Post
    template_name="myblog/supp.html"
    success_url= reverse_lazy('home')
    
    

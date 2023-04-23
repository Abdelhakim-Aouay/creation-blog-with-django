from django.urls import path
from . import views

urlpatterns = [
    
    path('home/', views.HomeListView.as_view(), name="home"),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name="article"),
]
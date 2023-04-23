from django.urls import path
from . import views

urlpatterns = [
    
    path('home/', views.HomeListView.as_view(), name="home"),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name="article"),
    path('add_post/', views.AddPostView.as_view(), name="add_post"),
    path('article/update_post/<int:pk>', views.UpdatePostView.as_view(), name="update_post"),
    path('article/supp_post/<int:pk>', views.DeletePostView.as_view(), name="supp"),
]

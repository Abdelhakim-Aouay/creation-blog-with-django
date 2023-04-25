from django.urls import path
from . import views

urlpatterns = [
    
    path('register/', views.UserRegisterView.as_view(), name="register"),
    path('login/', views.UserRegisterView.as_view(), name="login"),
    path('edit_profile/', views.UserEditView.as_view(), name="edit-profile"),

    
]

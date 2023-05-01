from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('register/', views.UserRegisterView.as_view(), name="register"),
    path('login/', views.UserRegisterView.as_view(), name="login"),
    path('edit_profile/', views.UserEditView.as_view(), name="edit-profile"),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', views.PasswordsChangeView.as_view()),

    
]

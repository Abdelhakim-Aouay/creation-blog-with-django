from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('register/', views.UserRegisterView.as_view(), name="register"),
    path('login/', views.UserRegisterView.as_view(), name="login"),
    path('edit_profile/', views.UserEditView.as_view(), name="edit-profile"),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', views.PasswordsChangeView.as_view()),
    path('<int:pk>/profile/', views.ShowProfileView.as_view(), name="show_profile"),
    path('<int:pk>/edit_profile_page/', views.EditProfilePageView.as_view(), name="edit_profile_page"),
    path('create_profile_page/', views.CreateProfileView.as_view(), name="create_profile_page"),



    
]

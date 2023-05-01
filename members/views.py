from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from .forms import SignUp, EditProfile
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class=SignUp
    template_name = "registration/register.html"
    success_url= reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class=EditProfile
    template_name = "registration/edit_profile.html"
    success_url= reverse_lazy('home')
    
    def get_object(self ):
        return self.request.user
    
    
class PasswordsChangeView(PasswordChangeView) :
    form_class=PasswordChangeForm
    template_name = "registration/change-password.html"
    success_url= reverse_lazy('home')
    
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .forms import SignUp
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class=SignUp
    template_name = "registration/register.html"
    success_url= reverse_lazy('login')

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUp(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    
    
            
    class Meta:
                model = User
                fields = ("username","first_name","last_name", "email", "password1", "password2")
        
    
    def __init__(self, *args, **kwargs):
        super(SignUp, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs['class']='form-control'
        self.fields["password1"].widget.attrs['class']='form-control'
        self.fields["password2"].widget.attrs['class']='form-control'
        
        
def fonction(*args):
        for arg in args:
            print(arg)
        
fonction(1, 2, 3, "quatre")

def fonction(**kwargs):
    for cle, valeur in kwargs.items():
        print(cle, valeur)
        
fonction(nom="Alice", age=25, ville="Paris")
            
            
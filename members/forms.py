from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from myblog.models import UserProfile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['bio', 'profile_pic', 'facebook', 'twitter', 'linkedin']
        widgets={
            
                'bio': forms.Textarea(attrs={'class' : 'form-control'}),
                #'profile_pic': forms.ImageField(attrs={'class' : 'form-control'}),
                'facebook': forms.TextInput(attrs={'class': 'form-control'}),
                'twitter': forms.TextInput(attrs={'class': 'form-control'}),
                'linkedin': forms.TextInput(attrs={'class': 'form-control'}),
            
            }

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
        
                    
class EditProfile(UserChangeForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    username=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_login=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    is_superuser=forms.CharField(max_length=100,required=False, widget=forms.CheckboxInput(attrs={'class' : 'form-check'}))
    is_active=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class' : 'form-check'}))
    is_staff=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class' : 'form-check'}))

    date_joined=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control'}))

    
    
            
    class Meta:
                model = User
                fields = ("username","first_name","last_name", "email", 'password',"is_superuser","last_login", "is_staff", "is_active", "is_staff", "date_joined")
            
            
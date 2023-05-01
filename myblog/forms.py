from django import forms
from .models import Post, Category

CHOIX=Category.objects.all().values_list('name', 'name') # la valeur 'name' représente la valeur stockée dans la base de données pour l'option "name" dans le champ category, tandis que 'name' est le libellé qui sera affiché à l'utilisateur dans les menus déroulants ou autres interfaces où le choix des categories est proposé.
# CHOIX = [('encoding', 'encoding'), ('sports', 'sports'), ('entertainemnt', 'entertainement')] : c'est pas dynamique don n'est pas interressant


choice_list=[]
for item in CHOIX:
    choice_list.append(item)

class AddForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=["title", 'title_tag', 'image', "author",  'category', "body"]
    
        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class' : 'form-control'}),
            #'header_image': forms.ImageField()
            'author': forms.TextInput(attrs={'class' : 'form-control', "value":"","id":"auteur", 'type': 'hidden'}),
            #'author': forms.Select(attrs={'class' : 'form-control'}),
            'category': forms.Select(choices=CHOIX,attrs={'class' : 'form-control'}),
            'body': forms.Textarea(attrs={'class' : 'form-control'})
        }
        
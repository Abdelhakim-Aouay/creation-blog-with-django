from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from six import python_2_unicode_compatible



@python_2_unicode_compatible
class Category(models.Model):
    name=models.CharField(max_length=100)
    
    class Meta:
            verbose_name = ("Category")
            verbose_name_plural = ("Categories")
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    bio=models.TextField()
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return str(self.user)


class Post(models.Model):
    title=models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    title_tag=models.CharField(max_length=100)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    #body=models.TextField()
    body=RichTextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=100, default="coding")
    Likes=models.ManyToManyField(User, related_name="blog_post")  # post can have many likes and user can have many likes also

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse("article", kwargs={"pk": self.pk}) # va redirect vers le page de l'article avec le pk creer 


from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    title=models.CharField(max_length=100)
    title_tag=models.CharField(max_length=100)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    

    

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse("article", kwargs={"pk": self.pk}) # va redirect vers le page de l'article avec le pk creer 


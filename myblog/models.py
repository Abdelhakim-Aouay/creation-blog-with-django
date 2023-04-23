from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    

    

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.title + ' | ' + str(self.author)

'''  def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk}) '''


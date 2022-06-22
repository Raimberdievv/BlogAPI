from tabnanny import verbose
from venv import create
from django.db import models
from apps.users.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.title 

class PostComment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)     
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий"    
        verbose_name_plural = "Комментарии"    
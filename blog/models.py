from django.db import models
from tinymce.models import HTMLField
from django.utils.html import format_html
# Create your models here.
class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="category/")

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return format_html("<image src = '/media/{}'style= width:50px;height:50px/>".format(self.image))



class Post(models.Model):
    pid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = HTMLField()
    url = models.CharField(max_length=100, unique=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post/")

    

    

    def __str__(self):
        return self.title
    



from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts')
    title = models.CharField(max_length=80)
    photo = models.ImageField('上传图片', upload_to='img', null=True, blank=True)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Review(models.Model):
    blog = models.ForeignKey(Post)
    user = models.CharField(max_length=254)
    img_url = models.CharField(max_length=100, null=True, default='', blank=True)
    email = models.CharField(max_length=100)
    content = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.blog.title


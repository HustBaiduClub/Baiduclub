from django.db import models

# Create your models here.


class Group(models.Model):
    group_img = models.ImageField(upload_to='img')
    group = models.CharField(max_length=50)
    intro = models.CharField(max_length=200)

    def __str__(self):
        return self.group
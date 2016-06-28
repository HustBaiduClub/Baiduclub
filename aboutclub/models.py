from django.db import models

# Create your models here.


class ClubIntro(models.Model):
    aspect = models.CharField(max_length=40)
    content = models.TextField(max_length=200)

    def __str__(self):
        return self.aspect
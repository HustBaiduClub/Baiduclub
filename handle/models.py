from django.db import models

# Create your models here.


class Handle(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    group = models.CharField(max_length=20)
    intro = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
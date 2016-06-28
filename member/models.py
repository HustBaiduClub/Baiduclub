from django.db import models
from django.contrib.auth.models import User
from group.models import Group
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    portrait = models.ImageField(upload_to='img')
    intro = models.TextField(max_length=200, null=True, blank=True)
    group = models.ForeignKey(Group, blank=True, null=True)
    github = models.CharField(max_length=100, null=True, blank=True)
    google_plus = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username

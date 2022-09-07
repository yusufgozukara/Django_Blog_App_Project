from distutils.command.upload import upload
from django.db import models
from django.contrib.auth import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'profile_pics/')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
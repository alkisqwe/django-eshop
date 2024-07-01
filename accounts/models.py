from django.contrib.auth.models import AbstractUser
from django.db import models

def productimages_path(instance, filename):
    return '{0}/{1}'.format(instance.pk, filename)

class CustomUser(AbstractUser):
    type = models.IntegerField(default=0)
    certified = models.IntegerField(default=0)
    profileimage = models.ImageField(upload_to=productimages_path, default="/media/default-profile.png")
    email = models.EmailField(unique=True)
    plan = models.IntegerField(default=0)

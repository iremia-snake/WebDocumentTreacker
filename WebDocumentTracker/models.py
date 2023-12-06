from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image
import random
import string

class Profile(models.Model):    # Профиль пользователя. Связан с таблицей пользователей один к одному
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    facebook = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)

    @receiver(post_save, sender=User)   # сигнал на создание пользователя
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)   # сигнал на сохранение пользователя
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    def __str__(self):
        return str(self.user)

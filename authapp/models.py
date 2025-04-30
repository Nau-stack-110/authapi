from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.utils.timezone import now, timedelta
import random

class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    tel = models.CharField(max_length= 20, unique=True)
    is_admin_coop = models.BooleanField(default=False)
    reset_pin = models.CharField(max_length=6, blank=True, null=True)
    pin_attempts = models.IntegerField(default=0)
    pin_expires_at = models.DateTimeField(null=True, blank=True)

    def generate_reset_pin(self):
        """Génère un PIN à 6 chiffres, définit une expiration et réinitialise les tentatives."""
        self.reset_pin = str(random.randint(100000, 999999)) 
        self.pin_attempts = 0 
        self.pin_expires_at = now() + timedelta(minutes=10)  
        self.save()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    bio  = models.CharField(max_length=300)
    image = models.ImageField(upload_to='users/', blank=True, null=True, default="default.jpg")
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullname
    
def create_user_profile(sender, instance, created, **kwargs):
     if created:
         Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)

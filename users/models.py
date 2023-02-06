from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=25, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_images', null=True, blank=True)

class WelcomePage(models.Model):
    welcome_greetings = models.CharField(max_length=300)
    welcome_picture = models.ImageField(upload_to="images", null=True, blank=True)
    
    def __unicode__(self):
        return self.welcome_greetings
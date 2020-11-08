from django.contrib.auth.models import User
from django.db import models
# from django.conf import settings

# AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
# AUTH_USER_MODEL



# Create your models here.
class Article(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    date = models.DateField(auto_now_add=True)
    body = models.TextField()
    link=  models.CharField(max_length=300,default='Unavailable')
    thumb = models.ImageField(default='default.png', blank=True)
    
    #

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:150]

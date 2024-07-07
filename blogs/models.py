from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Blog_app(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    blog_image =models.ImageField(upload_to='blogs/')
    date_added = models.DateTimeField(default=timezone.now)
    description = models.TextField(default='')
    
    def __str__(self):
        return self.title   
from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User 
from django.urls import reverse 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100) 
    content = models.TextField() 
    # image = models.ImageField(upload_to='blog_posts/', blank=True)
    date_posted = models.DateTimeField(default=timezone.now) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')  

    def __str__(self):
        return self.title 


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk}) 


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message  

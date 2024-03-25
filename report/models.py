from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone 

# Create your models here.
class PhotoReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False) 
    location = models.CharField(max_length=100, blank=False) 
    photo = models.ImageField(upload_to='photo_reports/')
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True) 
    DisplayFields = ['user', 'title', 'location', 'photo', 'description', 'timestamp']
    FilterFields = ['timestamp', 'location'] 

    def __str__(self):
        return self.title 

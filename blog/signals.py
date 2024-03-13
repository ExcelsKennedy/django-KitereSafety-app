from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Post, Notification

@receiver(post_save, sender=Post)
def create_notification(sender, instance, created, **kwargs):
    if created:
        users = User.objects.exclude(id=instance.author.id)  # Exclude the author from receiving notification
        for user in users:
            Notification.objects.create(user=user, post=instance, message="New blog post: {}".format(instance.title))

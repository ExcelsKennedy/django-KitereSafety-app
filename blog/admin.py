from django.contrib import admin
from .models import Post, Notification 

# Register your models here.
# admin.site.register(Post) 

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=Post.DisplayFields
    list_filter=Post.FilterFields 

# admin.site.register(Notification)  
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display=Notification.DisplayFields
    list_filter=Notification.FilterFields 
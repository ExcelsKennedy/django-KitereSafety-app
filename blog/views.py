from django.shortcuts import render 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
) 
from .models import Post, Notification
from django.utils import timezone
import pytz 

# Create your views here.

def home(request):
    posts = Post.objects.all()
    africa_nairobi_tz = pytz.timezone('Africa/Nairobi')
    
    # Convert datetime values for each post to Africa/Nairobi timezone
    for post in posts:
        post.date_posted = post.date_posted.astimezone(africa_nairobi_tz)
    
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)




class PostListView(ListView):
    model = Post 
    template_name = 'blog/home.html' 
    context_object_name = 'posts' 
    ordering = ['-date_posted'] 


class PostDetailView(DetailView):
    model = Post 


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post 
    fields = ['title', 'content'] 

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form) 


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Post 
    fields = ['title', 'content'] 

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object() 
        if self.request.user == post.author:
            return True 
        return False 


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    success_url = '/blog'

    def test_func(self):
        post = self.get_object() 
        if self.request.user == post.author:
            return True 
        return False 

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) 


def notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'blog/notifications.html', {'notifications': notifications}) 


def my_view(request):
    post =Post.objects.get(id=1)
    post_datetime_utc = post.created_at.astimezone(pytz.utc) 
    Africa_nairobi_tz = pytz.timezone('Africa/Nairobi') 
    post_datetime_nairobi = post_datetime_utc.astimezone(africa_nairobi_tz) 
    return render(request, 'blog/home.html', {'post_datetime': post_datetime_nairobi}) 
from django.contrib.auth import views as auth_views 
from django.urls import path

from . import views 
from .forms import LoginForm 

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('about/', views.about, name='about'),
    path('careers/', views.careers, name='careers'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
] 
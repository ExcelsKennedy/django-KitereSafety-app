from django.urls import path 
from . import views 
# from .views import photo_report_view


urlpatterns = [
    path('', views.report, name='report-home'),
    path('audio-report/', views.audio, name='audio-report'),
    path('photo-success/', views.photo_success, name='photo-success'),
    path('photo-report/', views.photo_report_view, name='photo-report'),
]

# from django.urls import path
# from .views import photo_report_view

# urlpatterns = [
#     path('photo-report/', photo_report_view, name='photo_report'),
#     # Other URLs...
# ]

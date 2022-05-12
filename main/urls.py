from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('all_info', views.all_info, name='all_info'),
    path('about', views.about, name='about'),
]


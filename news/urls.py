from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create_news, name='create_news'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsDetailUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDetailDeleteView.as_view(), name='news-delete'),
    path('house', views.house, name='house'),
    path('documents', views.documents, name='documents'),
    path('kids', views.kids, name='kids'),
    path('money', views.money, name='money'),
    path('animals', views.animals, name='animals'),
    path('israel', views.israel, name='israel'),
]


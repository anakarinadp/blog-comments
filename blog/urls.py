from django.urls import path
from blog import views

urlpatterns = [
    path('', views.accueil, name='accueil'), # url(r'^$', 'accueil', name='accueil'),
    path('<str:slug>/', views.lire_article, name='lire_article'),  # url(r'^(?P<slug>.+)$', 'lire_article', name='blog_lire'),
]

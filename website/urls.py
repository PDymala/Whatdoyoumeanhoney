from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:id>/',views.meme, name='meme'),
    path('submit', views.add_meme, name='submit'),
    path('', views.index, name='about'),
    path('search', views.search, name='search'),
    
]
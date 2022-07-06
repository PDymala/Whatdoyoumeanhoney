from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:id>/',views.meme, name='meme'),
    path('submit', views.add_meme, name='submit'),
    path('', views.index, name='about'),
    path('search', views.search, name='search'),
    path('your_memes', views.your_memes, name='your_memes'),
    path('meme_approval', views.meme_approval, name='meme_approval'),
    path('about', views.about, name='about'),
]
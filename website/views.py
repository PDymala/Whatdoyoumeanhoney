from django.shortcuts import render
from .models import  Meme

# Create your views here.

def index(request):
    memes = Meme.objects.all()
    return render(request, 'index.html', {'memes': memes

    })

def meme(request, id):
    meme = Meme.objects.get(id = id)

    return render(request, 'meme.html', {'meme': meme

    })
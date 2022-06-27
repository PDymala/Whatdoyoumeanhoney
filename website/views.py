from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import  Meme, User
from .forms import MemeForm
import datetime
from django.core.paginator import Paginator


# TODO filter tylko tych zaaprobowanych
def index(request):


    # memes = Meme.objects.all().order_by('add_date')
    p = Paginator(Meme.objects.filter(approved=True).order_by('add_date'), 10)
    # p = Paginator(Meme.objects.all().order_by('add_date'), 10)
    page = request.GET.get('page')
    memes = p.get_page(page)

    return render(request, 'index.html', {'memes': memes })

#TODO stronka z tymi do aprobacji, moze byc tabela z przyciskami i tekstem


def login(request):

    return render(request, 'login.html', { })

def meme(request, id):
    meme = Meme.objects.get(pk = id)

    return render(request, 'meme.html', {'meme': meme

    })
def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]

        memes = Meme.objects.filter(title__contains=searched)

        return render(request, 'search.html', {'searched': searched, 'memes': memes}) 
    else:
         return render(request, 'search.html', {}) 
    
def add_meme(request):
    subbmitted = False
    if request.method == "POST":
         form = MemeForm(request.POST)
         form.instance.add_date = datetime.datetime.now()
         form.instance.add_by = request.user

         if form.is_valid():
             form.save()
             return HttpResponseRedirect('/submit?subbmitted=True')
    else:
        form = MemeForm()
        if 'subbmitted' in request.GET:
            subbmitted = True
    return render(request, 'submit.html', {'form': form, 'subbmitted': subbmitted})

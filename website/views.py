import datetime
import os

import openai
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import MemeForm
from .models import Meme


# TODO filter tylko tych zaaprobowanych
def index(request):
    # memes = Meme.objects.all().order_by('add_date')
    p = Paginator(Meme.objects.filter(approved=True).order_by('-add_date'), 10)
    # p = Paginator(Meme.objects.all().order_by('add_date'), 10)
    page = request.GET.get('page')
    memes = p.get_page(page)

    return render(request, 'index.html', {'memes': memes})


# TODO stronka z tymi do aprobacji, moze byc tabela z przyciskami i tekstem


def login(request):
    return render(request, 'login.html', {})


def about(request):
    return render(request, 'about.html', {})


def meme(request, id):
    if request.method == "POST":
        messages.success(request, f"deleted {request.POST['delete']}")
        Meme.objects.filter(id=request.POST['delete']).delete()
        return redirect("home")
    else:
        meme = Meme.objects.get(pk=id)
        return render(request, 'meme.html', {'meme': meme})


def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]

        memes = Meme.objects.filter(title__contains=searched)

        return render(request, 'search.html', {'searched': searched, 'memes': memes})
    else:
        return render(request, 'search.html', {})


def your_memes(request):
    if request.user.is_authenticated:
        memes = Meme.objects.filter(add_by=request.user)

        return render(request, 'your_memes.html', {'memes': memes})
    else:
        return render(request, 'your_memes.html', {})


def getGPT(input):
    openai.api_key = os.environ.get('OPENAI_KEY', None)
    name_prompt = f"Write a hex color for prompt: {input}."
    name_response = openai.Completion.create(
        model="text-davinci-002",
        prompt=name_prompt,
        temperature=0.7,
        max_tokens=20,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    name = name_response['choices'][0]['text']
    return name


def meme_approval(request):
    if request.method == "POST":
        if 'approved' in request.POST:
            #    return HttpResponse(request.POST['approved'])

            #    print(Meme.objects.get(id = request.POST['approved']).prompt)
            text = getGPT(Meme.objects.get(id=request.POST['approved']).prompt)
            #    print(text)
            #    if isHex(text):
            Meme.objects.filter(id=request.POST['approved']).update(pantone=text)
            messages.success(request, f"approved {request.POST['approved']}")
            Meme.objects.filter(id=request.POST['approved']).update(approved=True)
            memes = Meme.objects.filter(approved=False)
            return render(request, 'meme_approval.html', {'memes': memes})
            #    else:

        #        messages.success(request, "error, try again" )
        #        memes = Meme.objects.filter(approved=False)
        #        return render(request, 'meme_approval.html', {'memes': memes}) 

        elif 'disapproved' in request.POST:
            #    return HttpResponse(request.POST['dissapproved'])
            messages.success(request, f"disapproved {request.POST['disapproved']}")
            Meme.objects.filter(id=request.POST['disapproved']).delete()
            memes = Meme.objects.filter(approved=False)
            return render(request, 'meme_approval.html', {'memes': memes})
        else:
            return render(request, '500.html', {})

    else:
        memes = Meme.objects.filter(approved=False)
        return render(request, 'meme_approval.html', {'memes': memes})


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

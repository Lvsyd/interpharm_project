from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    template = 'index.html'
    return render(request, template, context)


# View for About us
def o_nas(request):
    context = {}
    template = 'o_nas.html'
    return render(request, template, context)


def kontakt(request):
    context = {}
    template = 'kontakt.html'
    return render(request, template, context)


def sluzby(request):
    context = {}
    template = 'sluzby.html'
    return render(request, template, context)


def zakaznicka_zona(request):
    context = {}
    template = 'zakaznicka_zona.html'
    return render(request, template, context)


def zastupujuce_znacky(request):
    context = {}
    template = 'zastupujuce-znacky.html'
    return render(request, template, context)

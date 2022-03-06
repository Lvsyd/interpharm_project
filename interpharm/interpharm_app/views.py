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


from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    if "counter" not in request.session:
        request.session['counter'] = 1
    if 'random' not in request.session:
        request.session['random'] = get_random_string(length=14)
    return render(request, "random_words/index.html")

def reset(request):
    request.session['counter'] = 1
    return redirect(index)

def generate(request):
    request.session['random'] = get_random_string(length=14)
    request.session['counter'] = request.session['counter'] + 1 if 'counter' in request.session else 1
    return redirect(index)

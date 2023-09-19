from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(requests, *args, **kwargs):
    return HttpResponse("<h1>I love you Nada</h1>")
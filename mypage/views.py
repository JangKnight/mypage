from django.shortcuts import render
from django.http import HttpResponse

def me(request):
    return HttpResponse("<h1>About Me</h1>")


from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Django")

# Create your views here.
def welcome(request):
    return render(request,"demo.html")
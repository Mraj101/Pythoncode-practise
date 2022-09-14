from urllib import request
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.
def index(request):
    return  HttpResponse("Hello this is my first app")
    

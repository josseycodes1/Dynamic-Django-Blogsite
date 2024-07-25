from django.shortcuts import render

# Create your views here.

def home(request):
    return request(request, 'index.html')

def eachpost(request):
    return request(request, 'eachpost')

def allposts(request):
    return request(request, 'allposts')

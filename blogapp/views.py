from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def eachpost(request):
    return render(request, 'eachpost.html')

def allposts(request):
    return render(request, 'allposts.html')

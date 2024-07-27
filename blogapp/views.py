from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'blogapp/index.html')

def eachpost(request):
    return render(request, 'blogapp/eachpost.html')

def allposts(request):
    return render(request, 'blogapp/allposts.html')

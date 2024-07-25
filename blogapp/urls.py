from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('eachpost/', views.eachpost, name='eachpost'),
    path('allposts/', views.allposts, name='allposts'),
]
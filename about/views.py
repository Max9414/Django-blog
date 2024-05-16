from django.shortcuts import render
from django.views import generic
from .models import About

# Create your views here.

class PostList(generic.ListView):
    queryset = About.objects.all()
    template_name = "about/index.html"

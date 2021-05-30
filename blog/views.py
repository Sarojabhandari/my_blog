from blog.models import Post
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    posts= Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


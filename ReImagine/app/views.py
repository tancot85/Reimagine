from django.shortcuts import render
from django.http import HttpResponse
from . import ine
# from models import Post
from . import ine_component
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def content_page(request):
    posts = ine_component.get_posts('mumbai',10)
    return render(request, 'content.html', {'name_of_subreddit': 'mumbai', 'posts': posts})

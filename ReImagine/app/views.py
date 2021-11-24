from django.shortcuts import render
from django.http import HttpResponse, response
from . import ine
from . import ine_component
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def content_page(request):
    if(request.GET.get('data')):
        query = request.GET.get('data')
    else:
        query = 'ImaginaryLandscapes'
    posts = ine_component.get_posts(query,10)
    return render(request, 'content.html', {'name_of_subreddit': query, 'posts': posts})

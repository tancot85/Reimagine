from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm
from . import ine
from . import ine_component
#import wget
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def content_page(request):
    if(request.GET.get('data')):
        query = request.GET.get('data')
    else:
        query = 'ImaginaryLandscapes'
    posts = ine_component.get_posts(query, 10)
    return render(request, 'content.html', {'name_of_subreddit': query, 'posts': posts})


def login_user(request):
    if request.method == 'POST':  # if someone fills out form , Post it
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:  # if user exist
            login(request, user)
            messages.success(request, ('Youre logged in'))
            # routes to 'content on successful login
            return redirect('content')
        else:
            messages.success(request, ('Error logging in'))
            # re routes to login page upon unsucessful login
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('Youre now logged out'))
    return redirect('content')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Youre now registered'))
            return redirect('content')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'authenticate/register.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have edited your profile'))
            return redirect('content')
    else:  # passes in user information
        form = EditProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'authenticate/edit_profile.html', context)
    # return render(request, 'authenticate/edit_profile.html',{})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You have edited your password'))
            return redirect('content')
    else:  # passes in user information
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}
    return render(request, 'authenticate/change_password.html', context)

# def download_button(request):
#     q = request.GET.get()
#     print(q)
#     if(request.GET.GET('moredata')):
#         wget.download(request.GET.get('moredata'))
#     if(request.GET.get('title')):
#         query = request.GET.get('title')
#     else:
#         query = 'ImaginaryLandscapes'
#     posts = ine_component.get_posts(query,10)
#     return render(request, 'content.html', {'name_of_subreddit': query, 'posts': posts})

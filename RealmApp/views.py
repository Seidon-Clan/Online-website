from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, LoginForm, PostForm
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status= 1).order_by('-created_on')
    template_name = 'index.html'


def post_detail(request, slug):
    model = Post
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)

    return render(request, template_name, {'post': post})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username= username, password = raw_password)
            messages.success(request, f"Account created for {username}")
            return HttpResponse('Created')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form,})


def user_login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'],
                                password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('<h1>Welcome</h1>')
                else:
                    return HttpResponse("Blocked Blog")
            else:
                return  HttpResponse('User does not exists')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})


def about(request):
    return render(request, 'about.html')


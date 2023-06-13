from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.generic import View



def home(request):
    return render(request, 'main/main_page.html')

def teacher(request):
    return render(request, 'main/teacher.html')

@login_required
def web_technologies(request):
    return render(request, 'main/web-technologies.html')

@login_required
def informatyka(request):
    return render(request, 'main/informatyka.html')

@login_required
def OS_(request):
    return render(request, 'main/os.html')

@login_required
def news_main(request):
    return render(request, 'main/news-main.html')

@login_required
def show_news(request, content_slug):
    news_show = get_list_or_404(News, slug = content_slug)
    context = {
        'news_show': news_show,
    }
    return render(request, 'main/about_news.html', context)



def login_page(request):

    return render(request, 'main/login.html')

def loginView(request):
    if request.method == 'POST':
        username = request.POST["username_l"]
        password = request.POST["password_l"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            error = "неправильно введені дані"
            return render(request, 'main/login.html', {'error': error,})
    else:
        return render(request, 'main/index.html')


def Logout_user(request):
    logout(request)
    return redirect('login_page')

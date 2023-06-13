from django.shortcuts import get_list_or_404, render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *


@login_required
def home_web(request):

    return render(request, 'web_tech/mainpage_web.html')



@login_required
def lessons_web(request):
    value = request.GET.get('web_lesson')
    context = {
        'value': value,
    }
    return render(request, 'web_tech/pract_web/web_lesson_ext.html', context)
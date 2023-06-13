from django.shortcuts import get_list_or_404, redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
import random
import pickle


def Main_News_objects_(request):
    news = News.objects.all()

    return {'news': news,}
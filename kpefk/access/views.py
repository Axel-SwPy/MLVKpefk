from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import *
from .access_processor import *

@login_required
def home_access(request):
    context = {
    }
    return render(request, 'access/main_db.html', context)

@login_required
def entry_access(request):
    context = {
    }
    return render(request, 'access/entry_db.html', context)

@login_required
def lessons_db(request):
    value_db = request.GET.get("lesson")
    context = {
        'value_db': value_db,
    }
    return render(request, 'access/lessons_db/lesson_extend.html', context)





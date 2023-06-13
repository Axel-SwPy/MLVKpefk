from django.shortcuts import get_list_or_404, render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def main_excel(request):
    return render(request, 'excel/excel_main_page.html')

@login_required
def intro_excel(request):
    return render(request, 'excel/intro_excel.html')

@login_required
def about_excel(request):
    return render(request, 'excel/excel_2010.html')


@login_required
def control_work1(request):
    return render(request, 'excel/pract_excel/control_work_1.html')

@login_required
def control_work2(request):
    return render(request, 'excel/pract_excel/control_work_2.html')

@login_required
def practice_view(request):
    value = request.GET.get('practice')
    context = {
        'value': value,
    }
    return render(request, 'excel/pract_excel/pract_exc.html', context)


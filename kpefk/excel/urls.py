from django.urls import path
from . import views


urlpatterns = [
    path('excel', views.main_excel, name = 'excel'),
    path('excel/intro', views.intro_excel, name = 'intro_excel'),
    path('excel/about-Excel2010', views.about_excel, name = 'about_excel'),
    path('excel/practice_excel', views.practice_view, name= 'practice_view'),
    path('excel/control-work-1', views.control_work1, name= 'control_work1'),
    path('excel/control-work-2', views.control_work2, name= 'control_work2'),


]
from django.urls import path
from . import views
from .access_processor import *


urlpatterns = [
    #path('excel/practice_excel', views.practice_excel, name= 'practice_excel'),
    path('access/', views.home_access, name= "Access"),
    path('access/entry', views.entry_access, name= "entry_access"),
    path('access/lesson', views.lessons_db, name= "db_lesson"),

]
from django.urls import path
from . import views


urlpatterns = [
    path('web-technology', views.home_web, name = 'web_technology'),
    path('lesson-web', views.lessons_web, name= "lesson_web"),

]
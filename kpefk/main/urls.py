from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.home, name = 'home'),
    path('teacher', views.teacher, name = 'teacher'),
    path('news', views.news_main, name = 'news_main'),
    path('web-technologies', views.web_technologies, name = 'web_technologies'),
    path('informatyka', views.informatyka, name = 'informatyka'),
    path('operating_systems', views.OS_, name = 'os'),
    path('news/<slug:content_slug>', views.show_news, name='content'),


    path('login_page', views.login_page, name= "login_page"),
    path('login', views.loginView, name='login'),
    path('logout', views.Logout_user, name="log_out"),
]
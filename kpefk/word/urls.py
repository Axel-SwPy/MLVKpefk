from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('word', views.main_word, name = 'word'),
    path('word/intro', views.intro_word, name = 'intro_word'),
    path('word/about-Word2010', views.about_word, name = 'about_word'),
    path('word/practice/<int:main_cont_id>', views.show_practice, name = "practice"),
    path('word/<slug:choise_slug_img>', views.show_all_var, name='choise_img'),


    path('word/practice/controlquestions', PracticeQuestions.as_view(), name='word_questions'),
]
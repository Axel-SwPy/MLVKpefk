from django.shortcuts import get_list_or_404, redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
import random
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
import pickle



class CustomWordHTMX:
    def dispatch(self, request, *args, **kwargs):
        if not self.request.META.get('HTTP_HX_REQUEST'):
            self.template_name = 'word/practice/INC_control_questions.html'
        return super().dispatch(request, *args, **kwargs)




@login_required
def main_word(request):
    return render(request, 'word/word_main_page.html')

@login_required
def intro_word(request):
    return render(request, 'word/intro_word.html')

@login_required
def about_word(request):
    return render(request, 'word/word_2010.html')



def update():
    global slug_from_photo, list_links_variants
    slug_from_photo = Photo_variant.objects.values_list("slug_img", "img_connect_field__variant_name")
    list_links_variants = []

@login_required
def show_practice(request, main_cont_id):
    update()
    practice_per_id = Practice.objects.filter(id = main_cont_id)
    cont_all_page = Main_content.objects.filter(main_cont_id = main_cont_id)
    for slug_ in slug_from_photo:
        slug_img = slug_[0]
        slug_img = slug_img.rsplit("-")
        if slug_img[1] == str(main_cont_id):
            list_links_variants.append(["-".join(items for items in slug_img), slug_[1]])

    with open("list_links_variants.pickle", "wb") as f:
        pickle.dump(list_links_variants, f)

    link_slug = [slug[0] for slug in list_links_variants]

    random_variant = random.choice(link_slug) if link_slug else f"practice/{main_cont_id}"


    context = {
        'practice_per_id': practice_per_id,
        'cont_all_page': cont_all_page,
        'random_variant': random_variant,
        'main_cont_id': main_cont_id,
        }

    return render (request, 'word/practice/pract1.html', context)

@login_required
def show_all_var(request, choise_slug_img):
    list_variants = Photo_variant.objects.values_list("name_variant_img", "variant_img", "slug_img", "img_connect_field__variant_name", "img_connect_field__pract_var__practice_name")
    choose_variant = list_variants.filter(slug_img = choise_slug_img)
    choose_variant = choose_variant[int(choise_slug_img.rsplit('-')[1])-1]
    keys_var = ["name", "img", "link", "variant", "practice"]
    dict_variant_ = dict(zip(keys_var, choose_variant))


    with open("list_links_variants.pickle", "rb") as f:
        list_links_variants = pickle.load(f)
        keys_links = ['link_variant', 'name_variant']
        dict_links_variant = [dict(zip(keys_links, item)) for item in list_links_variants]

    link_slug = [slug[0] for slug in list_links_variants]
    context = {
        'list_links_variants': dict_links_variant,
        'choose_variant': dict_variant_,
    }
    random_variant = random.choice(link_slug)
    if random_variant is not None:
        context['random_variant'] = random_variant
    return render(request, 'word/practice/variants.html', context)




class PracticeQuestions(CustomWordHTMX, TemplateView):
    template_name = 'word/practice/control_questions.html'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            self.selected_practice = request.GET.get('pract_select')

        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        practice_data = Practice.objects.filter(id=self.selected_practice)

        context['practice_per_id'] = practice_data

        return context


    





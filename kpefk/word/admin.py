from django.contrib import admin
from .models import *


class PracticeAdmin(admin.ModelAdmin):
    list_display = ("id", "practice_name", "title_practice", "task")

class VerAdmin(admin.ModelAdmin):
    list_display = ("id", "variant_name")

class Photo_variantAdmin(admin.ModelAdmin):
    list_display = ("id", "name_variant_img", "slug_img", "variant_img", "img_connect_field")
    prepopulated_fields = {"slug_img": ("name_variant_img",)}

class MainCont_admin(admin.ModelAdmin):
    list_display = ("id", "title_name", "photo_word_cont", "main_cont")

admin.site.register(Variant, VerAdmin)
admin.site.register(Practice, PracticeAdmin)
admin.site.register(Main_content, MainCont_admin)
admin.site.register(Photo_variant, Photo_variantAdmin)
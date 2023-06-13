from django.db import models
from django.urls import reverse


class Photo_variant(models.Model):
    name_variant_img = models.CharField(unique=True, max_length = 250, verbose_name="Практична N, Варіант N")
    variant_img = models.ImageField(verbose_name="Зображення завдання", blank= True)
    img_connect_field = models.ForeignKey('Variant', on_delete=models.PROTECT, verbose_name="Звязок з таблицею")
    slug_img = models.SlugField(unique=True,verbose_name= "URL за зразком 'practice-N-variant-N', де N номер варіанта та практичної")

    def __str__(self):
        return self.name_variant_img
    
    def get_img_var_url(self):
        kwargs={'choise_slug_img': self.slug_img}
        return reverse('choise_img', kwargs)
    
    class Meta:
        verbose_name = "Фотографію"
        verbose_name_plural = "Фотографії варіантів"

class Variant(models.Model):
    variant_name = models.CharField(max_length = 100, db_index = True)
    pract_var = models.ManyToManyField('Practice', verbose_name="Звязок з таблицею")

    def __str__(self):
        return self.variant_name  
    
    class Meta:
        verbose_name = "Варіант"
        verbose_name_plural = "Варіанти робіт"
 

class Main_content(models.Model):
    title_name = models.TextField(verbose_name="<b>Запитання</b><br>Інструкція для вирішення питання")
    photo_word_cont = models.ImageField(verbose_name="Пояснююче зображення", blank= True)
    main_cont = models.ForeignKey('Practice', on_delete=models.PROTECT, verbose_name="Звязок з таблицею")

    def __str__(self):
        return self.title_name
    
    class Meta:
        verbose_name = "Вміст Практичної роботи"
        verbose_name_plural = "Вміст Практичних робіт"


class Practice(models.Model):
    practice_name = models.CharField(max_length= 100, db_index=True, verbose_name="Назва практичної 'Практична робота №'")
    title_practice = models.CharField(max_length = 255, verbose_name="Мета роботи")
    task = models.TextField(verbose_name="Завдання")
    control_questions = models.TextField(verbose_name= "контрольні запитання")

    def __str__(self):
        return self.practice_name
    
    def get_content_url(self):
        return reverse('practice', kwargs={'main_cont_id': self.pk})
    
    
    class Meta:
        verbose_name = "Практична роботу"
        verbose_name_plural = "Практичні роботи"

from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField(unique=True)
    content = models.TextField(blank = True)
    photo = models.ImageField()

    def __str__ (self):
        return self.title

    def get_url(self):
        return reverse('content', kwargs={'content_slug': self.slug})
    
    class Meta:
        verbose_name = "Новину"
        verbose_name_plural = "Новини"

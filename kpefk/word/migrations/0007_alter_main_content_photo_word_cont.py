# Generated by Django 4.1.4 on 2023-06-06 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0006_alter_photo_variant_variant_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_content',
            name='photo_word_cont',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Пояснююче зображення'),
        ),
    ]

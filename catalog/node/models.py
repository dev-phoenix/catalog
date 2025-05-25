from django.db import models

from category.models import Category

# Create your models here.
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models

# from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

'''
node
category
'''


# https://docs.djangoproject.com/en/5.0/topics/db/examples/many_to_many/
class Node(models.Model):
    '''
    title
    desc
    '''
    categories = models.ManyToManyField(Category, verbose_name='Категория')
    title = models.CharField( max_length=128, help_text='', verbose_name='Заголовок')
    path = models.CharField( max_length=128, help_text='', verbose_name='Путь')
    rating = models.IntegerField(help_text='Рейтинг')
    desc = models.TextField( help_text='', verbose_name='Описание')
    class Meta:
        db_table = 'node'
        ordering = ['-id']
        verbose_name = 'Статья'
        verbose_name_plural = "Статьи"
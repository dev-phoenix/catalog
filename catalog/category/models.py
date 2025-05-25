from django.db import models

# Create your models here.



class Category(models.Model):
    # parent
    # weiпht
    # name
    # key
    parent = models.ForeignKey('self', on_delete=models.SET_NULL,
                            blank=True, null=True, verbose_name='Родитель' )
    weight = models.IntegerField(help_text='Вес')
    name = models.CharField( max_length=64, help_text='', verbose_name='Название')
    key = models.CharField( max_length=64, help_text='', verbose_name='Ключ')

    class Meta:
        db_table = 'category'
        ordering = ['weight', 'name']
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"

    def __str__(self):
        return str(self.name) + f' #{self.key} '
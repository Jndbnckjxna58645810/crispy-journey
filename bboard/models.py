from django.db import models

class Bb(models.Model):
    person = models.ForeignKey("Salesman", null=True, on_delete=models.PROTECT, verbose_name='Продавец')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True,
verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True,
verbose_name='Опубликовано')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']

class Rubric(models.Model):
    name = models.CharField (max_length=20, db_index=True,
    verbose_name='Название')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

class Salesman(models.Model):
    person = models.TextField(null=True, blank=True, verbose_name='Продавец')
    phone = models.FloatField(null=True, blank=True, verbose_name='Номер телефона')

    def __str__(self):
        return self.person
    
    class Meta:
        verbose_name_plural = 'Продавцы'
        verbose_name = 'Продавец'
        ordering = ['person']
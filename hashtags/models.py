from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=30, verbose_name='Ваше имя?')
    phone = models.CharField(max_length=13, default='+996', verbose_name='ваш номер')
    email = models.EmailField(verbose_name='Укажите эмейл', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.created_at}'


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Укажите тег')

    def __str__(self):
        return f'#{self.name}'


class Content(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название контенка')
    image = models.ImageField(upload_to='content/')
    tags = models.ManyToManyField(Tag, related_name='content_tags', null=True)

    def __str__(self):
        return self.name



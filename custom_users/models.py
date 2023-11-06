from django.db import models
from django.contrib.auth.models import User

MALE = 1
FEMALE = 2

GENDER_TYPE = (
    (MALE, "Муж"),
    (FEMALE, "Жен")
)

YES = 1
NO = 2

CRIMINAL_RECORD = (
    (YES, "Да"),
    (NO, "Нет")
)

MARRIED = 1
FREE = 2

MARRY = (
    (MARRIED, 'Да'),
    (FREE, 'Нет')
)

class CustomUser(User):
    phone_number = models.CharField(max_length=13, verbose_name='Введите номер телефона')
    date_birth = models.DateField(verbose_name='Дата рождения')
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Выбирите пол')
    pet = models.CharField(max_length=100, verbose_name='Имя вашего домашнего животного')
    year = models.IntegerField(verbose_name='Введите ваш возраст')
    hobby = models.CharField(max_length=20, verbose_name='Ваше хобби')
    job = models.CharField(max_length=25, verbose_name='Кем вы работате/учитесь')
    criminal_record = models.IntegerField(choices=CRIMINAL_RECORD, verbose_name='Были ли вы ранее судимы?')
    married = models.IntegerField(choices=MARRY, verbose_name='Женаты/замужем ли вы?')


class RegisterSucces(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title

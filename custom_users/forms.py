from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

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


class CustomRegForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, label='Укажите ваш номер')
    date_birth = forms.DateField(required=True, label='Дата рождения', widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True, label='Выбирите пол')
    pet = forms.CharField(required=True, label='Имя вашего домашнего животного')
    year = forms.IntegerField(required=True, label='Введите ваш возраст')
    hobby = forms.CharField(required=True, label='Ваше хобби')
    job = forms.CharField(required=True, label='Кем вы работате/учитесь')
    criminal_record = forms.ChoiceField(choices=CRIMINAL_RECORD, required=True, label='Были ли вы ранее судимы?')
    married = forms.ChoiceField(choices=MARRY, required=True, label='Женаты/замужем ли вы?')

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "phone_number",
            "date_birth",
            "gender",
            "pet",
            "year",
            "hobby",
            "job",
            "criminal_record",
            "married",
        )

    def save(self, commit=True):
        user = super(CustomRegForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
# Generated by Django 4.2.6 on 2023-11-05 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterSucces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='criminal_record',
            field=models.IntegerField(choices=[(1, 'Да'), (2, 'Нет')], default=0, verbose_name='Были ли вы ранее судимы?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='hobby',
            field=models.CharField(default=0, max_length=20, verbose_name='Ваше хобби'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='job',
            field=models.CharField(default=0, max_length=25, verbose_name='Кем вы работате/учитесь'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='married',
            field=models.IntegerField(choices=[(1, 'Да'), (2, 'Нет')], default=0, verbose_name='Женаты/замужем ли вы?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='pet',
            field=models.CharField(default=0, max_length=100, verbose_name='Имя вашего домашнего животного'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='year',
            field=models.IntegerField(default=0, verbose_name='Введите ваш возраст'),
            preserve_default=False,
        ),
    ]

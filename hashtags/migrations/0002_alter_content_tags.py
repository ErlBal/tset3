# Generated by Django 4.2.7 on 2023-11-06 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashtags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='content_tags', to='hashtags.tag'),
        ),
    ]

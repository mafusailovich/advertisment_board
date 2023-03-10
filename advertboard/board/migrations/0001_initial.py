# Generated by Django 4.1.5 on 2023-01-15 13:31

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(help_text='Заголовок', max_length=255)),
                ('content', ckeditor.fields.RichTextField(blank=True, help_text='Содержание', null=True)),
                ('rating', models.IntegerField(default=0, help_text='Рейтинг', null=True)),
                ('count', models.IntegerField(default=0, help_text='Количество комментариев', null=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Здесь напишите ваш отклик')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('acceptresponse', models.BooleanField(default=False, help_text='Принят ли отклик')),
                ('advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.advertisment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название категории', max_length=255)),
                ('subscribers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='advertisment',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.category'),
        ),
        migrations.AddField(
            model_name='advertisment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

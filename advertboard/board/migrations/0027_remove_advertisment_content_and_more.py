# Generated by Django 4.1.5 on 2023-01-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0026_advertisment_content_upload_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisment',
            name='content',
        ),
        migrations.AlterField(
            model_name='advertisment',
            name='category',
            field=models.CharField(choices=[('Танки', 'Танки'), ('Торговцы', 'Торговцы'), ('Квестгиверы', 'Квестгиверы'), ('Хилы', 'Хилы'), ('ДД', 'ДД'), ('Мастера заклинаний', 'Мастера заклинаний'), ('Зельевары', 'Зельевары'), ('Кожевники', 'Кожевники'), ('Кузнецы', 'Кузнецы'), ('Гилдмастеры', 'Гилдмастеры')], default='Танки', max_length=255),
        ),
    ]
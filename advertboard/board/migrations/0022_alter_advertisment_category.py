# Generated by Django 4.1.5 on 2023-01-18 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0021_alter_advertisment_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='category',
            field=models.CharField(choices=[('Квестгиверы', 'Квестгиверы'), ('Танки', 'Танки'), ('Торговцы', 'Торговцы'), ('Зельевары', 'Зельевары'), ('Хилы', 'Хилы'), ('Кузнецы', 'Кузнецы'), ('Кожевники', 'Кожевники'), ('ДД', 'ДД'), ('Мастера заклинаний', 'Мастера заклинаний'), ('Гилдмастеры', 'Гилдмастеры')], default='Танки', max_length=255),
        ),
    ]
# Generated by Django 4.1.5 on 2023-01-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0011_alter_advertisment_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='category',
            field=models.CharField(blank=True, choices=[(3, 'ДД'), (7, 'Кузнецы'), (4, 'Торговцы'), (6, 'Квестгиверы'), (1, 'Танки'), (10, 'Мастера заклинаний'), (9, 'Зельевары'), (8, 'Кожевники'), (5, 'Гилдмастеры'), (2, 'Хилы')], max_length=255),
        ),
    ]

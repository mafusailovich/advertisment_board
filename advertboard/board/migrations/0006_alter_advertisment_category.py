# Generated by Django 4.1.5 on 2023-01-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_alter_advertisment_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='category',
            field=models.CharField(choices=[(1, 'Танки'), (9, 'Зельевары'), (6, 'Квестгиверы'), (5, 'Гилдмастеры'), (2, 'Хилы'), (8, 'Кожевники'), (4, 'Торговцы'), (7, 'Кузнецы'), (10, 'Мастера заклинаний'), (3, 'ДД')], max_length=255),
        ),
    ]

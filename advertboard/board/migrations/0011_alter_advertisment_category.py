# Generated by Django 4.1.5 on 2023-01-16 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_delete_category_alter_advertisment_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='category',
            field=models.CharField(blank=True, choices=[(7, 'Кузнецы'), (2, 'Хилы'), (10, 'Мастера заклинаний'), (8, 'Кожевники'), (5, 'Гилдмастеры'), (4, 'Торговцы'), (9, 'Зельевары'), (1, 'Танки'), (6, 'Квестгиверы'), (3, 'ДД')], max_length=255),
        ),
    ]

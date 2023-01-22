# Generated by Django 4.1.5 on 2023-01-16 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0016_remove_advertisment_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisment',
            name='category',
            field=models.CharField(choices=[(9, 'Зельевары'), (4, 'Торговцы'), (10, 'Мастера заклинаний'), (2, 'Хилы'), (6, 'Квестгиверы'), (7, 'Кузнецы'), (1, 'Танки'), (3, 'ДД'), (5, 'Гилдмастеры'), (8, 'Кожевники')], default=1, max_length=255),
        ),
    ]

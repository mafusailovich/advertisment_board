# Generated by Django 4.1.5 on 2023-01-22 10:24

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0025_alter_advertisment_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisment',
            name='content_upload',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='advertisment',
            name='category',
            field=models.CharField(choices=[('Кожевники', 'Кожевники'), ('Хилы', 'Хилы'), ('Квестгиверы', 'Квестгиверы'), ('Зельевары', 'Зельевары'), ('Гилдмастеры', 'Гилдмастеры'), ('Кузнецы', 'Кузнецы'), ('Мастера заклинаний', 'Мастера заклинаний'), ('ДД', 'ДД'), ('Танки', 'Танки'), ('Торговцы', 'Торговцы')], default='Танки', max_length=255),
        ),
    ]

# Generated by Django 3.2.15 on 2022-11-07 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foto',
            name='foto_category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='foto',
        ),
    ]

# Generated by Django 4.1.2 on 2023-01-25 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP2', '0012_cartdb_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartdb',
            name='Image',
        ),
    ]
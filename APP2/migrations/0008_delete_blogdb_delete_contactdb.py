# Generated by Django 4.1.2 on 2023-01-04 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP2', '0007_blogdb'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blogdb',
        ),
        migrations.DeleteModel(
            name='Contactdb',
        ),
    ]
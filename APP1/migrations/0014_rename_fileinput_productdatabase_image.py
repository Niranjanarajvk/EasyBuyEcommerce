# Generated by Django 4.1.2 on 2023-01-03 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0013_rename_image_productdatabase_fileinput'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdatabase',
            old_name='FileInput',
            new_name='Image',
        ),
    ]

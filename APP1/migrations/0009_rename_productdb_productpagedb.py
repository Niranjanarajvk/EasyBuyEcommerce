# Generated by Django 4.1.2 on 2023-01-02 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0008_rename_productpagedb_productdb'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='productdb',
            new_name='productpagedb',
        ),
    ]

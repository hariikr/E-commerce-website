# Generated by Django 5.0.6 on 2024-06-16 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_catagory_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Catagory',
        ),
    ]

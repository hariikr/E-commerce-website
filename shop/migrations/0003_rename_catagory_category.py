# Generated by Django 5.0.6 on 2024-06-16 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_favourite_product_remove_favourite_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catagory',
            new_name='Category',
        ),
    ]

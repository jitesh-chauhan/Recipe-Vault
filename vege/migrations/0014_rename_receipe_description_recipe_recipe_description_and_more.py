# Generated by Django 5.0.2 on 2024-04-23 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0013_rename_receipe_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='receipe_description',
            new_name='recipe_description',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='receipe_img',
            new_name='recipe_img',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='receipe_name',
            new_name='recipe_name',
        ),
    ]

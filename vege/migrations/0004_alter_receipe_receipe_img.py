# Generated by Django 5.0.2 on 2024-03-17 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0003_alter_receipe_receipe_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='receipe_img',
            field=models.ImageField(upload_to='static/receipe_img'),
        ),
    ]

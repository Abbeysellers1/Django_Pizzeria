# Generated by Django 3.0.5 on 2022-12-11 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_auto_20221210_2357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='text',
            new_name='pizza_name',
        ),
    ]

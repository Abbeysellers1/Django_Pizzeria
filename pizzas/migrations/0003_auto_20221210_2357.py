# Generated by Django 3.0.5 on 2022-12-11 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_auto_20221210_2354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='pizza_name',
            new_name='text',
        ),
    ]
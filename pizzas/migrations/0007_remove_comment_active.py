# Generated by Django 3.0.5 on 2022-12-11 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0006_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
    ]

# Generated by Django 2.0.3 on 2018-04-11 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fides', '0006_projectpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpage',
            name='title',
        ),
    ]

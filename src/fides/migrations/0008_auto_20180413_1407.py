# Generated by Django 2.0.3 on 2018-04-13 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fides', '0007_remove_projectpage_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='status',
        ),
        migrations.AddField(
            model_name='project',
            name='wizard_step',
            field=models.IntegerField(default=1),
        ),
    ]

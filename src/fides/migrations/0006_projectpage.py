# Generated by Django 2.0.3 on 2018-04-10 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fides', '0005_auto_20180410_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('url', models.URLField(unique=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fides.Project')),
            ],
        ),
    ]
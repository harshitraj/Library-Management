# Generated by Django 3.0.5 on 2023-07-13 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentextra',
            name='email',
        ),
    ]

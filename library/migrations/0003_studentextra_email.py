# Generated by Django 3.0.5 on 2023-07-13 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_remove_studentextra_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentextra',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]

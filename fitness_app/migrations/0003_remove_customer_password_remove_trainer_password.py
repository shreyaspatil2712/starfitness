# Generated by Django 4.0.10 on 2023-08-25 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0002_logindata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='password',
        ),
    ]

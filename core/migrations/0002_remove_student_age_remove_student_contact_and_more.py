# Generated by Django 4.2 on 2023-05-01 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.RemoveField(
            model_name='student',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
    ]
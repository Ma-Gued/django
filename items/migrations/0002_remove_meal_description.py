# Generated by Django 5.1.1 on 2024-10-08 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='description',
        ),
    ]

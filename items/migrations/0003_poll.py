# Generated by Django 5.1.1 on 2024-10-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_remove_meal_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
            ],
        ),
    ]

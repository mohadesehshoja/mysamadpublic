# Generated by Django 5.0.6 on 2024-05-19 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0007_uni_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uni',
            name='restaurant',
        ),
    ]

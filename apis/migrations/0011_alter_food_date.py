# Generated by Django 5.0.6 on 2024-05-19 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0010_alter_uni_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='date',
            field=models.DateField(),
        ),
    ]

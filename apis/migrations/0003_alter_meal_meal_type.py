# Generated by Django 5.0.6 on 2024-05-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_food_date_food_meal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='meal_type',
            field=models.CharField(choices=[('lunch', 'lunch'), ('dinner', 'dinner')]),
        ),
    ]

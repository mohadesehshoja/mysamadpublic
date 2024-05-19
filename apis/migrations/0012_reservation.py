# Generated by Django 5.0.6 on 2024-05-19 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0011_alter_food_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservs', models.ManyToManyField(related_name='reservations', to='apis.food')),
            ],
        ),
    ]
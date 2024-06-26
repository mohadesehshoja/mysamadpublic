# Generated by Django 5.0.6 on 2024-05-19 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='meal',
            field=models.ManyToManyField(related_name='foods', to='apis.meal'),
        ),
    ]

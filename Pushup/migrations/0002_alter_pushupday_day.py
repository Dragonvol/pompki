# Generated by Django 4.0.5 on 2022-06-18 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pushup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pushupday',
            name='day',
            field=models.DateField(),
        ),
    ]
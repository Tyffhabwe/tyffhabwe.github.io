# Generated by Django 3.0.4 on 2020-04-01 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_taken',
            field=models.FloatField(),
        ),
    ]
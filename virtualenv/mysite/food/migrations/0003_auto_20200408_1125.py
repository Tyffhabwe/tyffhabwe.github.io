# Generated by Django 3.0.4 on 2020-04-07 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20200402_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='time_taken',
        ),
        migrations.AddField(
            model_name='post',
            name='article_link',
            field=models.CharField(default='None', max_length=500),
        ),
    ]

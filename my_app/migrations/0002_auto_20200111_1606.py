# Generated by Django 2.2.5 on 2020-01-11 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='event',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

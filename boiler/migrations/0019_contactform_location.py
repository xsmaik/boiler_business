# Generated by Django 5.1.7 on 2025-04-08 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boiler', '0018_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='location',
            field=models.CharField(default='', max_length=255, verbose_name='Локация'),
        ),
    ]

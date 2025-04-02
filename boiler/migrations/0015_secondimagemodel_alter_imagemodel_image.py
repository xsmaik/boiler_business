# Generated by Django 5.1.7 on 2025-04-02 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boiler', '0014_imagemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second_image', models.ImageField(upload_to='uploads/', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Изображение для следующей страницы',
                'verbose_name_plural': 'Изображения для следующей страницы',
            },
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(upload_to='uploads/', verbose_name='Изображение'),
        ),
    ]

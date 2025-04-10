# Generated by Django 5.1.7 on 2025-04-02 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boiler', '0009_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='TitleThirdPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_third', models.CharField(max_length=100, verbose_name='Название тайтла')),
                ('description_third', models.TextField(default='Нет описания', max_length=300, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Тайтл-3',
                'verbose_name_plural': 'Тайтлы-3',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
